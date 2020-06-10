"""

We can use a Python function to compute the objective
(symbolic computation with variable object) and that function can also be used alone or within a constraint:

"""

from docplex.mp.model import Model

def compute_cost(nbBus40,nbBus30):
   return 500.0*nbBus40+400.0*nbBus30;

def compute_cost2(nbBus40,nbBus30):
   return 500*nbBus40+300*nbBus30;

print("naive way without optimization : 8 buses 40 seats")
print("cost = ",compute_cost(8,0))
print()

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')

mdl.minimize(compute_cost(nbbus40,nbbus30))

print("Option 1")
             
mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)
    
print("cost = ",compute_cost(nbbus40.solution_value,nbbus30.solution_value))
    

mdl.minimize(compute_cost2(nbbus40,nbbus30))

print()
print("Option 2")
             
mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("cost = ",compute_cost2(nbbus40.solution_value,nbbus30.solution_value))

