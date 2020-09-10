#How to count the number of constraints that are true and set a constraint
#on this value

from docplex.mp.model import Model

# Data

Buses=[
    (40,500),
    (30,400),
    (35,450),
    (20,300)
    ]

nbKids=300

# Indexes

busSize=0;
busCost=1;

for b in Buses:
    print("buses with ",b[busSize]," seats cost ",b[busCost])

print()    

mdl = Model(name='buses')

#decision variables
mdl.nbBus=mdl.integer_var_dict(Buses,name="nbBus")

# Constraint
mdl.add_constraint(mdl.sum(mdl.nbBus[b]*b[busSize] for b in Buses) >= nbKids, 'kids')

# Objective
mdl.minimize(sum(mdl.nbBus[b]*b[busCost] for b in Buses))

mdl.solve()

# Display solution
for b in Buses:
    print(mdl.nbBus[b].solution_value," buses with ",b[busSize]," seats");

#Add a constraint
# Number of sizes where we have 1 or 2 buses should be at least 3

mdl.add(sum(mdl.logical_and(1<=mdl.nbBus[b],mdl.nbBus[b]<=2) for b in Buses) >=3)

mdl.solve()

print()
print("Number of sizes where we have 1 or 2 buses should be at least 3")
print()

# Display solution
for b in Buses:
    print(mdl.nbBus[b].solution_value," buses with ",b[busSize]," seats");

"""

which gives

buses with  40  seats cost  500
buses with  30  seats cost  400
buses with  35  seats cost  450
buses with  20  seats cost  300

5.0  buses with  40  seats
1.0  buses with  30  seats
2.0  buses with  35  seats
0  buses with  20  seats

Number of sizes where we have 1 or 2 buses should be at least 3

4.0  buses with  40  seats
1.0  buses with  30  seats
2.0  buses with  35  seats
2.0  buses with  20  seats

"""
