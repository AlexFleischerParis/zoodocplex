

from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*460 + nbbus30*360)

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print()
print("with the logical constraint")

nbKindOfBuses = mdl.integer_var(name='nbKindOfBuses')
mdl.add(nbKindOfBuses==(nbbus40>=1)+(nbbus30>=1))

mdl.minimize(nbbus40*460 + nbbus30*360+(nbKindOfBuses-1)*(500))

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0

with the logical constraint
nbBus40  =  0
nbBus30  =  10.0
nbKindOfBuses  =  1.0

"""
