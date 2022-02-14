

from docplex.mp.model import Model

mdl = Model(name='buses')

schoolwithminimum9buses=1

nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_integer_vars():
   print(v," = ",v.solution_value)

print()
print("with schoolwithminimum9buses=1")

#if then constraint
if (schoolwithminimum9buses==1):
   mdl.add(nbbus40+nbbus30>=9)
else:
   mdl.add(nbbus40+nbbus30>=0)
   
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

 

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value) 

'''

which gives

nbBus40  =  6.0
nbBus30  =  2.0

with schoolwithminimum9buses=1
nbBus40  =  3
nbBus30  =  6

'''
