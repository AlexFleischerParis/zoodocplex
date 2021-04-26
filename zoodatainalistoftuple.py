from docplex.mp.model import Model

# Data

Buses=[
    (40,500),
    (30,400)
    ]

nbKids=300

# Indexes

busSize=0;
busCost=1;

for b in Buses:
    print("buses with ",b[busSize]," seats cost ",b[busCost])

mdl = Model(name='buses')

#decision variables
mdl.nbBus=mdl.integer_var_dict(Buses,name="nbBus")

# Constraint
mdl.add_constraint(mdl.sum(mdl.nbBus[b]*b[busSize] for b in Buses) >= nbKids, 'kids')

# Objective
mdl.minimize(mdl.sum(mdl.nbBus[b]*b[busCost] for b in Buses))

mdl.solve()

# Display solution
for b in Buses:
    print(mdl.nbBus[b].solution_value," buses with ",b[busSize]," seats"); 

"""

which gives

buses with  40  seats cost  500
buses with  30  seats cost  400
6.0  buses with  40  seats
2.0  buses with  30  seats

"""
