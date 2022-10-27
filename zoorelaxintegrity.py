"""

Now let's see how easy it is to relax integrity
constraints and turn a MIP into LP, solve and get
dual value (shadow price)

"""
from docplex.mp.model import Model
from docplex.mp.relax_linear import LinearRelaxer

def make_bus_model():
    mdl = Model(name='buses')
    nbbus40 = mdl.integer_var(name='nbBus40')
    nbbus30 = mdl.integer_var(name='nbBus30')

    mdl.add_constraint(nbbus40 * 40 + nbbus30 * 30 >= 300, 'kids')
    mdl.minimize(nbbus40 * 500 + nbbus30 * 400)
    return mdl

if __name__ == '__main__':
    bm1 = make_bus_model()
    bm1.print_information()
    s1 = bm1.solve(log_output=True)
    s1.display()

    bmr = LinearRelaxer.make_relaxed_model(bm1)
    bmr.print_information()
    rs = bmr.solve(log_output=True)
    rs.display()

    duals = bmr.get_constraint_by_name("kids").dual_value

    print("dual of the 300 kids constraint = ",duals)

    for v in bmr.iter_continuous_vars():
       print(v," = ",v.solution_value)
       rc=v.reduced_cost
       print("reduced cost =",rc)

"""

which gives

solution for: buses
objective: 3800
nbBus40 = 6
nbBus30 = 2
Model: lp_buses
 - number of variables: 2
   - binary=0, integer=0, continuous=2
 - number of constraints: 1
   - linear=1
 - parameters: defaults
 - objective: minimize
 - problem type is: LP
Version identifier: 12.10.0.0 | 2019-11-26 | 843d4de2ae
CPXPARAM_Read_DataCheck                          1
CPXPARAM_RandomSeed                              201903125
Tried aggregator 1 time.
LP Presolve eliminated 1 rows and 2 columns.
All rows and columns eliminated.
Presolve time = 0.00 sec. (0.00 ticks)
solution for: lp_buses
objective: 3750.000
nbBus40 = 7.500
dual of the 300 kids constraint =  12.5

nbBus40  =  7.5
reduced cost = 0
nbBus30  =  0
reduced cost = 25.0

And we can confirm that if we use only 40 seats buses the marginal cost of a seat within a 40 seats bus is costbus40/40=12.5
And that if we remove 25 to the price for 30 seats buses then they are as cheap as 40 seats buses.


"""
