

from docplex.mp.model import Model
from pandas import *

# Data

dfBuses = pandas.DataFrame({'size': [40,30], 'cost': [500,400]},
                      index = ['bus1', 'bus2'], columns=['size','cost'])

print(dfBuses)

nbKids=300

for b in dfBuses.itertuples():
    print("buses with ",b.size," seats cost ",b.cost)

mdl = Model(name='buses')

#decision variables
mdl.nbBus=mdl.integer_var_dict(dfBuses.itertuples(),name="nbBus")

# Constraint
mdl.add_constraint(sum(mdl.nbBus[b]*b.size for b in dfBuses.itertuples()) >= nbKids, 'kids')

# Objective
mdl.minimize(sum(mdl.nbBus[b]*b.cost for b in dfBuses.itertuples()))

mdl.solve()

# Dislay solution
for b in dfBuses.itertuples():
    print(mdl.nbBus[b].solution_value," buses with ",b.size," seats")
