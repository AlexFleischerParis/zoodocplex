from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')
mdl.add(nbbus40*40 + nbbus30*30 >= 300)
mdl.minimize(nbbus40*500 + nbbus30*400)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 

mdlclone=mdl.clone()
mdlequal=mdl;


# set upper bound for nbbus40 to 0
mdl.add(nbbus40==0)

msolclone=mdlclone.solve()
msolequal=mdlequal.solve()


print("clone")
print(msolclone['nbBus40']," buses 40 seats")
print(msolclone['nbBus30']," buses 30 seats") 

print("= operator")
print(msolequal['nbBus40']," buses 40 seats")
print(msolequal['nbBus30']," buses 30 seats") 

'''

which gives

clone
6  buses 40 seats
2  buses 30 seats
= operator
0  buses 40 seats
10  buses 30 seats

'''



