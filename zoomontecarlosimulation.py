

import random
import math

random.seed(1)

nbKids=300
costBus40=500.0;
costBus30=400.0;

nbSamples=20
nbMaxKidsAbsent=30;


nbKidsLess=[random.randint(0,nbMaxKidsAbsent) for i in range(0,nbSamples)]
nbKidsOptions=[nbKids-nbKidsLess[i] for i in range(0,nbSamples)]

#To compute the average cost per kid of each bus

averageCost40=costBus40/40;
averageCost30=costBus30/30;

#naïve computation, use the cheapest bus

cheapestCostPerKid=min(averageCost40,averageCost30)
cheapestBusSize=40 if (cheapestCostPerKid==averageCost40) else 30
cheapestBusCost=costBus40 if (cheapestCostPerKid==averageCost40) else costBus30

nbBusNeeded=[int(math.ceil(nbKidsOptions[i]/cheapestBusSize)) for i in range(0,nbSamples)]

cost=[cheapestBusCost*nbBusNeeded[i] for i in range(0,nbSamples)] ;

print("cost = ",cost);

averageCost=1/nbSamples*sum([cost[i] for i in range(0,nbSamples)])


print("------------------------------");
print("average cost = ",math.ceil(averageCost));

"""

which gives

cost =  [4000.0, 4000.0, 3500.0, 3500.0, 3500.0, 4000.0, 4000.0, 4000.0, 4000.0, 3500.0, 4000.0, 4000.0, 3500.0, 4000.0, 3500.0, 4000.0, 4000.0, 4000.0, 4000.0, 3500.0]
------------------------------
average cost =  3825

"""
