from docplex.mp.model import Model
from docplex.mp.progress import *

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.parameters.mip.limits.solutions=1

while (1==1):
    sol=mdl.solve(log_output=False)
    for v in mdl.iter_integer_vars():
       print(v," = ",v.solution_value)

    print("objective = ",sol.get_objective_value())
    print("best bound = ",mdl.solve_details.best_bound)
    print("mip gap = ",mdl.solve_details.mip_relative_gap)  
       
    print("status : ",mdl.solve_details.status)   
    if ("optimal solution" in str(mdl.solve_details.status)):
        break


"""

nbBus40  =  8.0
nbBus30  =  0
objective =  4000.0
best bound =  0.0
mip gap =  0.999999999999975
status :  solution limit exceeded
nbBus40  =  7.0
nbBus30  =  1.0
objective =  3900.0
best bound =  3750.0
mip gap =  0.03846153846153748
status :  solution limit exceeded
nbBus40  =  6.0
nbBus30  =  2.0
objective =  3800.0
best bound =  3800.0
mip gap =  0.0
status :  integer optimal solution


"""
