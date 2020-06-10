

from docplex.cp.model import CpoModel

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

mdl = CpoModel(name='buses')

#decision variables
mdl.nbBus=mdl.integer_var_dict(Buses,0,1000,name="nbBus")

# Constraint
mdl.add(sum(mdl.nbBus[b]*b[busSize] for b in Buses) >= nbKids)

# Objective
mdl.minimize(sum(mdl.nbBus[b]*b[busCost] for b in Buses))

msol=mdl.solve()

# Dislay solution
for b in Buses:
    print(msol[mdl.nbBus[b]]," buses with ",b[busSize]," seats"); 
