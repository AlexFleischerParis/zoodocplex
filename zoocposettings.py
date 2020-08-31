from docplex.cp.model import CpoModel
from docplex.cp.model import CpoParameters

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')
mdl.add(nbbus40*40 + nbbus30*30 >= 300)
mdl.minimize(nbbus40*500 + nbbus30*400)

param=CpoParameters();
param.set_TimeLimit(20)
param.TimeLimit=20;

#use parameters param for model mdl
mdl.set_parameters(param)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats")

#read params from model mdl
param2=mdl.get_parameters()

print("time limit = " ,param2["TimeLimit"])
print("time limit = " ,param2.get_attribute("TimeLimit"))

for i in param2:
    print(i," = ",param2[i])


"""
which gives
6  buses 40 seats
2  buses 30 seats
time limit =  20
time limit =  20
TimeLimit  =  20
"""
