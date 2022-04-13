from docplex.mp.model import Model 

Buses=[
    (40,500),
    (30,400)
    ]

nbKids=300
nbSizes=len(Buses)

# Indexes

busSize=0;
busCost=1;

for b in Buses:
    print("buses with ",b[busSize]," seats cost ",b[busCost])

mdl = Model(name='buses')

#decision variables

mdl.nbBus = mdl.integer_var_list(nbSizes,0,1000,name="nbBus")


# Constraint
mdl.add(sum(mdl.nbBus[b]*Buses[b][busSize] for b in range(0,nbSizes)) >= nbKids)

# Objective
mdl.minimize(sum(mdl.nbBus[b]*Buses[b][busCost] for b in range(0,nbSizes)))

msol=mdl.solve()

# Dislay solution
for b  in range(0,nbSizes):
    print(msol[mdl.nbBus[b]]," buses with ",Buses[b][busSize]," seats")

"""

gives

buses with  40  seats cost  500
buses with  30  seats cost  400
6.0  buses with  40  seats
2.0  buses with  30  seats

"""

