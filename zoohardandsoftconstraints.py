from docplex.mp.model import Model
from docplex.mp.relaxer import Relaxer

from docplex.mp.conflict_refiner import ConflictRefiner

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')

mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
ctbus=mdl.add_constraint(nbbus40 + nbbus30 <= 7, 'nbBus')

# make ctbus a hard constraint (cannot be relaxed)
ctbus.set_mandatory()

mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

mdl.report()
print(f"* solve status is: '{mdl.solve_details.status}'") #infeasible model

print()
print("------- starting relaxation")
print()

rx = Relaxer()
rx.relax(mdl)

print ("number_of_relaxations= " + str(rx.number_of_relaxations))
rx.print_information()

mdl.report()
print(f"* status after relaxation is: {mdl.solve_details.status}")
#print(mdl.solution)

print()
print("------ starting conflict refiner")
print()

cr=ConflictRefiner()
conflicts=cr.refine_conflict(mdl)
conflicts.display()


# for conflict in conflicts:
#     st = conflict.status
#     ct = conflict.element
#     label = conflict.name
#     label_type = type(conflict.element)
#     if isinstance(conflict.element, VarLbConstraintWrapper) \
#             or isinstance(conflict.element, VarUbConstraintWrapper):
#         ct = conflict.element.get_constraint()
#
#     # Print conflict information in console
#     print("Conflict involving constraint: %s" % label)
#     print(" \tfor: %s" % ct)

"""

which gives

------- starting relaxation

Warning: 1 constraint(s) will not be relaxed (e.g.: nbBus: nbBus40+nbBus30 <= 7)
number_of_relaxations= 1
* number of relaxations: 1
 - relaxed: kids, with relaxation: -20.0
* total absolute relaxation: 20.0
* model buses solved with objective = 3500
* status after relaxation is: optimal relaxed sum of infeasibilities

------ starting conflict refiner

conflict(s): 2
  - status: Member, LinearConstraint: kids: 40nbBus40+30nbBus30 >= 300
  - status: Member, LinearConstraint: nbBus: nbBus40+nbBus30 <= 7

  """
