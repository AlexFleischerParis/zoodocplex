

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
print("with if nb buses 40 more than 3  then nbBuses30 more than 7")

#logical constraint
mdl.add((nbbus40>=3)<=(nbbus30>=7))
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

 


for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value) 

'''

which gives

nbBus40  =  6.0
nbBus30  =  2.0

with if nb buses 40 more than 3  then nbBuses30 more than 7
nbBus40  =  0
nbBus30  =  10.0

'''
