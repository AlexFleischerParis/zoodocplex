

from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')

# and suppose we need to order quantities
# that should be 3 multipliers

mdl.add(nbbus40 % 3==0)
mdl.add(nbbus30 % 3==0)

mdl.add(nbbus40*40 + nbbus30*30 >= 300)
mdl.minimize(nbbus40*500 + nbbus30*400)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 


"""

which gives

6  buses 40 seats
2  buses 30 seats

"""
