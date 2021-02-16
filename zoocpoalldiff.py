

from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')
nbbus50 = mdl.integer_var(0,1000,name='nbBus50')
mdl.add(nbbus40*40 + nbbus30*30 + 50*nbbus50>= 120)

mdl.add(mdl.all_diff(nbbus50,nbbus40,nbbus30))

mdl.minimize(nbbus50*500+nbbus40*400 + nbbus30*300)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats")
print(msol[nbbus50]," buses 50 seats") 


"""

which gives

0  buses 40 seats
1  buses 30 seats
2  buses 50 seats

"""
