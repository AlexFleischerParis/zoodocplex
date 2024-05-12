from docplex.mp.model import Model

mdl = Model(name='buses')

nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')


mdl.parameters.mip.limits.solutions=2;

mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)



sol=mdl.solve(log_output=True,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("objective = ",sol.get_objective_value())
print("best bound = ",mdl.solve_details.best_bound)
print("mip gap = ",abs(sol.get_objective_value()-mdl.solve_details.best_bound)/(abs(1e-10+sol.get_objective_value())))
print("mip gap = ",mdl.solve_details.mip_relative_gap)  

"""
nbBus40  =  7.0
nbBus30  =  1.0
objective =  3900.0
best bound =  3800.0
mip gap =  0.025641025641024984
mip gap =  0.025641025641024984
"""