from docplex.mp.model import Model
import pandas as pd

buses = {'costBus40': [500, 550,600], 'costBus30': [400, 450,440],'nbKids': [300, 320,330]}
dfBusesScenarii = pd.DataFrame(data=buses)



for s in range(0,len(dfBusesScenarii)):
    costBus40=dfBusesScenarii['costBus40'][s]
    costBus30=dfBusesScenarii['costBus30'][s]
    nbKids=dfBusesScenarii['nbKids'][s]

    mdl = Model(name='buses')
    
    nbbus40 = mdl.integer_var(name='nbBs40')
    nbbus30 = mdl.integer_var(name='nbBus30')

    mdl.add_constraint(nbbus40*40 + nbbus30*30 >= nbKids, 'kids')
    mdl.minimize(nbbus40*costBus40 + nbbus30*costBus30)

    mdl.solve()
    cost=mdl.solution.get_objective_value()
    
    print("if we need to bring ",nbKids," kids  to the zoo");
    print("with costs ",costBus40," and ",costBus30)
    print(int(nbbus40.solution_value)," buses 40 seats and ",int(nbbus30.solution_value), " buses 30 seats");
    print("cost = ",cost)
    print()

"""

gives

if we need to bring  300  kids  to the zoo
with costs  500  and  400
6  buses 40 seats and  2  buses 30 seats
cost =  3800.0

if we need to bring  320  kids  to the zoo
with costs  550  and  450
8  buses 40 seats and  0  buses 30 seats
cost =  4400.0

if we need to bring  330  kids  to the zoo
with costs  600  and  440
0  buses 40 seats and  11  buses 30 seats
cost =  4840.0

"""
