#How to count the number of values


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

maxquantity=10

#decision variables
mdl.nbBus=mdl.integer_var_dict(Buses,0,maxquantity,name="nbBus")

# Constraint
mdl.add_constraint(mdl.sum(mdl.nbBus[b]*b[busSize] for b in Buses) >= nbKids, 'kids')

# Objective
mdl.minimize(sum(mdl.nbBus[b]*b[busCost] for b in Buses))

mdl.solve()

# Display solution
for b in Buses:
    print(mdl.nbBus[b].solution_value," buses with ",b[busSize]," seats");

#Add a constraint
# Number of different quantity should be less than 1

mdl.add(mdl.sum((mdl.sum((q==mdl.nbBus[b]) for b in Buses)>=1) for q in range(0,maxquantity+1)) <=1)

mdl.solve()

print()
print("Number of sizes where we have 1 possible quantity ")
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

6.0  buses with  40  seats
2.0  buses with  30  seats
0  buses with  35  seats
0  buses with  20  seats

Number of sizes where we have 1 possible quantity 

3.0  buses with  40  seats
3.0  buses with  30  seats
3.0  buses with  35  seats
3.0  buses with  20  seats

"""
