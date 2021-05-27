# Here let's see how to tell CPLEX
# to branch fisrt on nbBus40 and then on nbBus30

from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')

mdl.cplex.order.set([(nbbus40.index,100,0),(nbbus30.index,0,0)])

mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=True,)

mdl.export("c:\\temp\\buses.lp")
mdl.cplex.order.write("c:\\temp\\zoo.ord")

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)


"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0

and in zoo.ord

NAME             Priority Order
    nbBus40                     100
    nbBus30                       0
ENDATA

"""
