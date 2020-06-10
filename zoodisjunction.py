

from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_integer_vars():
   print(v," = ",v.solution_value)

print()
print("with nb buses 40 less than 3 or more than 7")

option1=mdl.binary_var(name='option1')
option2=mdl.binary_var(name='option2')

mdl.add(option1==(nbbus40<=3))
mdl.add(option2==(nbbus40>=7))

mdl.add(1==mdl.logical_or(option1,option2))

mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

'''

which gives

nbBus40  =  6.0
nbBus30  =  2.0

with nb buses 40 less than 3 or more than 7
nbBus40  =  7.0
nbBus30  =  1.0

'''
