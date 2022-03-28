from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

print("objective = ",mdl.objective_value)

print("NNZ = ",mdl.solve_details.nb_linear_nonzeros)
print("gap = ",mdl.solve_details.mip_relative_gap)
print("problem type = ",mdl.solve_details.problem_type)
print("status = ",mdl.solve_details.status)
print("status_code = ",mdl.solve_details.status_code)

"""

gives

objective =  3800.0
NNZ =  2
gap =  0.0
problem type =  MILP
status =  integer optimal solution
status_code =  101

"""
