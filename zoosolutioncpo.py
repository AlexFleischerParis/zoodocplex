from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')
mdl.add(nbbus40*40 + nbbus30*30 >= 300)
mdl.minimize(nbbus40*500 + nbbus30*400)

msol=mdl.solve()

print("objective = ",msol.get_objective_values()[0])
print("Solution status = ", msol.get_solve_status())
print("number of constraints = ",msol.solver_infos.get_number_of_constraints())
print("gap = ",msol.get_objective_gap())

"""

gives

objective =  3800
Solution status =  Optimal
number of constraints =  1
gap =  0

"""

