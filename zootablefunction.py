

from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')


costBus40=[0,500,995,1480,1900,2350,2750,3100,3520,3900,4200];
costBus30=[0,400,780,1180,1570,1960,2350,2650,2950,3200,3600];

nbbus40 = mdl.integer_var(0,11,name='nbBus40')
nbbus30 = mdl.integer_var(0,11,name='nbBus30')
mdl.add(nbbus40*40 + nbbus30*30 >= 300)

#table function objective
mdl.minimize(mdl.element(costBus40,nbbus40) + mdl.element(costBus30,nbbus30))

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 


"""

which gives

7  buses 40 seats
1  buses 30 seats

"""
