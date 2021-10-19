from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')

nbbus=nbbus40+nbbus30
mdl.add_kpi(nbbus,"nbbus")

mdl.add(nbbus40*40 + nbbus30*30 >= 300)
mdl.minimize(nbbus40*500 + nbbus30*400)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats")

print("nbbus = ",msol["nbbus"])

"""

6  buses 40 seats
2  buses 30 seats
nbbus =  8

"""
