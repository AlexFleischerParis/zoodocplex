#How to count the number of values


from docplex.cp.model import CpoModel

# Data

Buses=[
    (40,500),
    (30,400),
    (35,450),
    (20,300)
    ]

nbKids=300
maxquantity=10

# Indexes

busSize=0;
busCost=1;

for b in Buses:
    print("buses with ",b[busSize]," seats cost ",b[busCost])

print()    

for b in Buses:
    print("buses with ",b[busSize]," seats cost ",b[busCost])

mdl = CpoModel(name='buses')

#decision variables
mdl.nbBus=mdl.integer_var_dict(Buses,0,maxquantity,name="nbBus")


# Constraint
mdl.add(sum(mdl.nbBus[b]*b[busSize] for b in Buses) >= nbKids)

# Objective
mdl.minimize(sum(mdl.nbBus[b]*b[busCost] for b in Buses))

msol=mdl.solve()

# Dislay solution
for b in Buses:
    print(msol[mdl.nbBus[b]]," buses with ",b[busSize]," seats");

#Add a constraint
# Number of different quantity should be less than 1

mdl.add(mdl.sum(((mdl.count(mdl.nbBus.values(),q)>=1) for q in range(0,maxquantity+1)))<=1)

#mdl.add(mdl.sum((mdl.sum((q==mdl.nbBus[b]) for b in Buses)>=1) for q in range(0,maxquantity+1)) <=1)
# works too but less CP style

msol2=mdl.solve()

print()
print("Number of sizes where we have 1 possible quantity ")
print()

# Display solution

for b in Buses:
    print(msol2[mdl.nbBus[b]]," buses with ",b[busSize]," seats");

"""

which gives

umber of sizes where we have 1 possible quantity 

3  buses with  40  seats
3  buses with  30  seats
3  buses with  35  seats
3  buses with  20  seats

"""

 
