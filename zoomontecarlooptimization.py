

import random
import math

random.seed(1)

from docplex.mp.model import Model

# original model

nbKids=300
mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
costBus40=500.0;
costBus30=400.0;
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= nbKids, 'kids')
mdl.minimize(nbbus40*costBus40 + nbbus30*costBus30)

nbSamples=20
nbMaxKidsAbsent=30;

nbKidsLess=[random.randint(0,nbMaxKidsAbsent) for i in range(0,nbSamples)]
nbKidsOptions=[nbKids-nbKidsLess[i] for i in range(0,nbSamples)]

#Monte Carlo optimization

totalCost=0.0;
for i in range(0,nbSamples):
    
   mdl.get_constraint_by_name("kids").rhs=nbKidsOptions[i]
   mdl.solve()
   cost=mdl.solution.get_objective_value()
   totalCost+=cost
   print("if we need to bring ",nbKidsOptions[i]," kids  to the zoo");
   print("cost = ",cost)

print()   
averageCost=1/nbSamples*totalCost


print("------------------------------");
print("average cost = ",math.ceil(averageCost));

"""

which gives



average cost =  3665 

So the school knows 3665 is the figure they could use instead of 3825

4% saving in the budget in that toy example.

But the conclusion is Monte Carlo optimization is pretty simple and helps do more with less. 

"""
