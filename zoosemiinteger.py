'''

let's see how easy moving to use semiinteger and semicontinuous decision variables with docplex.

Semiinteger means for example for a quantity of buses that it's either 0 or within a given range.

In our bus example, suppose we cannot rent less than 4 buses for any given size.

We then write:

'''

from docplex.mp.model import Model

# original model

mdl = Model(name='buses')
nbbus40 = mdl.semiinteger_var(4,20,name='nbBus40')
nbbus30 = mdl.semiinteger_var(4,20,name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_semiinteger_vars():
    print(v," = ",v.solution_value)

'''

which gives

nbBus40  =  4.0
nbBus30  =  5.0

'''
