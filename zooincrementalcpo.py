import numpy as np
np.bool = np.bool_

from docplex.cp.model import CpoModel


mdl = CpoModel(name='buses')
mdl.set_parameters(LogVerbosity='Quiet')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')
ct1=(nbbus40*40 + nbbus30*30 >= 300)
mdl.add(ct1)
obj1=mdl.minimize(nbbus40*500 + nbbus30*400)
mdl.add(obj1)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 

mdl.remove(obj1)
mdl.remove(ct1)
obj2=mdl.minimize(nbbus40*450 + nbbus30*400)
# 40 sets buses now cost 350
# and we have 350 kids
print("And now 450 for 40 seats buses and 350 kids")
ct2=(nbbus40*40 + nbbus30*30 >= 350)
mdl.add(ct2)
mdl.add(obj2)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 


"""

which gives

6  buses 40 seats
2  buses 30 seats
And now 450 for 40 seats buses and 350 kids
8  buses 40 seats
1  buses 30 seats

"""
