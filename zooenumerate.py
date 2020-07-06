

from docplex.mp.model import Model

from cplex.exceptions import CplexError, CplexSolverError

def make_bus_model(**kwargs):
    mdl = Model(name='buses', **kwargs)
    nbbus40 = mdl.integer_var(name='nbBus40')
    nbbus30 = mdl.integer_var(name='nbBus30')
    mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
    mdl.minimize(nbbus40*460 + nbbus30*360)
    mdl.parameters.mip.pool.intensity=4
    mdl.apply_parameters()
    return mdl


def generate_soln_pool(mdl):
    cpx = mdl.get_cplex()
    try:
        cpx.populate_solution_pool()
    except CplexSolverError:
        print("Exception raised during populate")
        return []
    numsol = cpx.solution.pool.get_num()
    print("The solution pool contains %d solutions." % numsol)
    meanobjval = cpx.solution.pool.get_mean_objective_value()
    print("The average objective value of the solutions is %.10g." %
          meanobjval)

    nb_vars = mdl.number_of_variables
    sol_pool = []
    for i in range(numsol):
        objval_i = cpx.solution.pool.get_objective_value(i)

        x_i = cpx.solution.pool.get_values(i)
        assert len(x_i) == nb_vars
        sol = mdl.new_solution()
        for k in range(nb_vars):
            vk = mdl.get_var_by_index(k)
            sol.add_var_value(vk, x_i[k])
        sol_pool.append(sol)
    return sol_pool

if __name__ == "__main__":
    bm = make_bus_model()
    pool = generate_soln_pool(bm)
    for s, sol in enumerate(pool,start=1):
        print(" this is solution #{0} of the pool".format(s))
        sol.display()

"""

which gives

The solution pool contains 28 solutions.
The average objective value of the solutions is 4437.857143.
 this is solution #1 of the pool
solution for: buses
nbBus40 = 6
nbBus30 = 2
 this is solution #2 of the pool
solution for: buses
nbBus40 = 7
nbBus30 = 1
 this is solution #3 of the pool
solution for: buses
nbBus40 = 6
nbBus30 = 3
 this is solution #4 of the pool
solution for: buses
nbBus40 = 7
nbBus30 = 2
 this is solution #5 of the pool
solution for: buses
nbBus40 = 9
nbBus30 = -0
 this is solution #6 of the pool
solution for: buses
nbBus40 = 6
nbBus30 = 4
 this is solution #7 of the pool
solution for: buses
nbBus40 = 8
nbBus30 = 1
 this is solution #8 of the pool
solution for: buses
nbBus40 = 7
nbBus30 = 3
 this is solution #9 of the pool
solution for: buses
nbBus40 = 10
nbBus30 = -0
 this is solution #10 of the pool
solution for: buses
nbBus40 = 6
nbBus30 = 5
 this is solution #11 of the pool
solution for: buses
nbBus40 = 9
nbBus30 = 1
 this is solution #12 of the pool
solution for: buses
nbBus40 = 5
nbBus30 = 4
 this is solution #13 of the pool
solution for: buses
nbBus40 = 11
nbBus30 = -0
 this is solution #14 of the pool
solution for: buses
nbBus40 = 8
nbBus30 = 2
 this is solution #15 of the pool
solution for: buses
nbBus40 = 7
nbBus30 = 4
 this is solution #16 of the pool
solution for: buses
nbBus40 = 6
nbBus30 = 6
 this is solution #17 of the pool
solution for: buses
nbBus40 = 10
nbBus30 = 1
 this is solution #18 of the pool
solution for: buses
nbBus40 = 9
nbBus30 = 2
 this is solution #19 of the pool
solution for: buses
nbBus40 = 12
nbBus30 = -0
 this is solution #20 of the pool
solution for: buses
nbBus40 = 8
nbBus30 = 3
 this is solution #21 of the pool
solution for: buses
nbBus40 = 4
nbBus30 = 5
 this is solution #22 of the pool
solution for: buses
nbBus40 = 6
nbBus30 = 7
 this is solution #23 of the pool
solution for: buses
nbBus40 = 9
nbBus30 = 3
 this is solution #24 of the pool
solution for: buses
nbBus40 = 3
nbBus30 = 6
 this is solution #25 of the pool
solution for: buses
nbBus40 = 10
nbBus30 = 2
 this is solution #26 of the pool
solution for: buses
nbBus40 = 11
nbBus30 = 1
 this is solution #27 of the pool
solution for: buses
nbBus40 = 5
nbBus30 = 5
 this is solution #28 of the pool
solution for: buses
nbBus40 = 8
nbBus30 = 0

"""
