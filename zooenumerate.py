

from docplex.mp.model import Model

from cplex.exceptions import CplexError, CplexSolverError

def make_bus_model(**kwargs):
    mdl = Model(name='buses', **kwargs)
    nbbus40 = mdl.integer_var(name='nbBus40')
    nbbus30 = mdl.integer_var(name='nbBus30')
    mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
    mdl.minimize(nbbus40*460 + nbbus30*360)
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

The solution pool contains 3 solutions.
The average objective value of the solutions is 3580.
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
nbBus40 = 8
nbBus30 = 0

"""
