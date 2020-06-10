"""

 In Constraint Programming decision variables have to be integer but sometimes we need more than this.

Let's see how we can handle through decision expressions.

Suppose in the bus example we want to book not only whole buses but also percentage of buses.

Then we can write

"""



from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')

#now suppose we can book a % of buses not only complete buses

scale=100
scalenbbus40 = mdl.integer_var(0,1000,name='scalenbBus40')
scalenbbus30 = mdl.integer_var(0,1000,name='scalenbBus30')

nbbus40= scalenbbus40 / scale
nbbus30= scalenbbus30 / scale

 

mdl.add(nbbus40*40 + nbbus30*30 >= 310)
mdl.minimize(nbbus40*500 + nbbus30*400)

msol=mdl.solve()

print(msol[scalenbbus40]/scale," buses 40 seats")
print(msol[scalenbbus30]/scale," buses 30 seats")

"""

which gives

7.75  buses 40 seats
0.0  buses 30 seats

"""
