

from docplex.mp.model import Model
from pandas import *


# Data

dfBuses = pandas.DataFrame({'size': [40,30], 'cost': [500,400]},
                          index = ['bus1', 'bus2'], columns=['size','cost'])
print(dfBuses)
print(dfBuses.shape[0])

nbKids=300

for b in dfBuses.itertuples():
    print("buses with ",b.size," seats cost ",b.cost)

mdl = Model(name='buses')

nbBusesTypes=dfBuses.shape[0]


#decision variables

mdl.nbBus = mdl.integer_var_list(nbBusesTypes,0,1000,name="nbBus")


# Constraint
mdl.add(mdl.sum(mdl.nbBus[b]*dfBuses.iloc[b][0] for b in range(0,nbBusesTypes)) >= nbKids)

# Objective
mdl.minimize(mdl.sum(mdl.nbBus[b]*dfBuses.iloc[b][1] for b in range(0,nbBusesTypes)))

msol=mdl.solve()

# Dislay solution
for b  in range(0,nbBusesTypes):
    print(msol[mdl.nbBus[b]]," buses with ",dfBuses.iloc[b][0]," seats"); 
