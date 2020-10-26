#Now suppose we can rent only 0,1,3,4 or 5 buses of 40 seats bu

from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')
mdl.add(nbbus40*40 + nbbus30*30 >= 300)
mdl.minimize(nbbus40*500 + nbbus30*400)

allowedQuantities=[0,1,3,4,5];
nbbus40.set_domain(allowedQuantities)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 


"""

which gives

3  buses 40 seats
6  buses 30 seats

"""
