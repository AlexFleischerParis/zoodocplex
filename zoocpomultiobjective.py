from docplex.cp.model import CpoModel
from docplex.cp.model import CpoParameters

mdl = CpoModel(name='buses')

param=CpoParameters()
param.OptimalityTolerance=0.01
mdl.set_parameters(param)

nbbus50 = mdl.integer_var(0,10,name='nbBus50')
nbbus40 = mdl.integer_var(0,10,name='nbBus40')
nbbus30 = mdl.integer_var(0,10,name='nbBus30')
cost = mdl.integer_var(0,10000,name='cost')
co2emission = mdl.integer_var(0,10000,name='co2emission')

mdl.add(nbbus50*50+nbbus40*40 + nbbus30*30 >= 200)
mdl.add(co2emission==nbbus50*10+nbbus40*11+nbbus30*12)
mdl.add(cost==nbbus40*500 + nbbus30*400+nbbus50*625)
mdl.add(mdl.minimize_static_lex([cost,co2emission]))
msol=mdl.solve()

print(msol[nbbus50]," buses 50 seats") 
print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 
print("cost = ",msol[cost])
print("co2 emission = ",msol[co2emission]/10) 

"""

4  buses 50 seats
0  buses 40 seats
0  buses 30 seats
cost =  2500
co2 emission =  4.0

"""
