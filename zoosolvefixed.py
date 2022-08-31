"""

Shadow price or dual price is the improvement in the contribution or costs by having 
one additional unit of a  resource which is causing a bottleneck.

In linear programming, reduced cost, or opportunity cost, is the amount by which 
an objective function coefficient would have to improve (so increase 
for maximization problem, decrease for minimization problem) before it
 would be possible for a corresponding variable to assume a positive value in 
 the optimal solution. (Wikipedia)

 """

from docplex.mp.model import Model
from docplex.mp import with_funcs 

mdl = Model(name='buses')
nbbus40 = mdl.continuous_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')

mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=True,)
 
print("Initial model")
print("objective = ",mdl.objective_value)
print()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)
for v in mdl.iter_continuous_vars():
    print(v," = ",v.solution_value) 

print("solvefixed")
with with_funcs.model_solvefixed(mdl) as mdl2:
  mdl2.solve()
   
  
  print("objective = ",mdl2.objective_value)
  duals = mdl2.get_constraint_by_name("kids").dual_value
  print("dual of the 300 kids constraint = ",duals)
  rc = nbbus30.reduced_cost
  print("reduced cost of nbbus30 = ",rc)



"""

which gives

Initial model
objective =  3750.0

nbBus30  =  0
nbBus40  =  7.5
solvefixed
objective =  3750.0
dual of the 300 kids constraint =  12.5
reduced cost of nbbus30 =  25.0

"""
