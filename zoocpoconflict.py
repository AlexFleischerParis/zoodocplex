import numpy as np
np.bool = np.bool_

from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')

nbKidsConstraint = (nbbus40*40 + nbbus30*30 >= 300)
nbKidsConstraint.set_name("nbKids")
mdl.add(nbKidsConstraint)

maxTotalBuses=(nbbus40 + nbbus30 <= 7)
maxTotalBuses.set_name("maxTotalBuses")
mdl.add(maxTotalBuses)
mdl.minimize(nbbus40*500 + nbbus30*400)

res=msol=mdl.solve()

print(res.get_solve_status())

conf=mdl.refine_conflict()
confConstraints=conf.get_all_member_constraints()

print("We have a conflict betwee, : ")
for i in confConstraints:
    print(i)




"""

which gives

! Conflict status           : Terminated normally, conflict found
 ! Conflict size             : 2 constraints
 ! Number of iterations      : 5
 ! Total memory usage        : 658.3 kB
 ! Conflict computation time : 0.03s
 ! ----------------------------------------------------------------------------
We have a conflict with :
nbKids = nbBus40 * 40 + nbBus30 * 30 >= 300
maxTotalBuses = nbBus40 + nbBus30 <= 7

"""
