
from docplex.mp.model import Model



nbKids=300
nbKidsScenarii=[nbKids+i*10 for i in range(-10,3)]
nbKidsProba=[ 1, 1, 2, 2, 2 ,3 ,3 ,4,  5 ,10 ,50 ,10, 7]
nbScenarii=len(nbKidsScenarii)

assert sum(nbKidsProba)==100



mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
costBus40=500.0;
costBus30=400.0;

nbKidsMax=max(nbKidsScenarii)

ctKid=mdl.add_constraint(nbbus40*40 + nbbus30*30 >= nbKidsMax, 'kids')
mdl.minimize(nbbus40*costBus40 + nbbus30*costBus30)

mdl.solve()

print("Robust 100%")
for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("objective = ",mdl.objective_value)

costIncreaseIfLastMinute=1.1



print()
print("Now stochastic with cost increase if last minute ",costIncreaseIfLastMinute)

mdl.remove_constraints([ctKid])
nbBus40onTop = mdl.integer_var_list(nbScenarii,name="nbBus40onTop")
nbBus30onTop = mdl.integer_var_list(nbScenarii,name="nbBus30onTop")
mdl.minimize(nbbus40*costBus40 + nbbus30*costBus30+costIncreaseIfLastMinute*\
             (\
             mdl.sum(1/100*nbKidsProba[s]*(costBus40*nbBus40onTop[s]+costBus30*nbBus30onTop[s])\
             for s in range(0,nbScenarii))))

for s in range(0,nbScenarii):
   mdl.add_constraint(((nbbus40+nbBus40onTop[s])*40 + (nbbus30+nbBus30onTop[s])*30 >= nbKidsScenarii[s]))


mdl.solve()

for v in mdl.iter_integer_vars():
    if (round(v.solution_value)!=0):
       print(v," = ",int(round(v.solution_value)))

print("objective = ",mdl.objective_value)

"""

which gives

Robust 100%
nbBus40  =  8.0
nbBus30  =  0
objective =  4000.0

Now stochastic with cost increase if last minute  1.1
nbBus40  =  6
nbBus40onTop_8  =  1
nbBus40onTop_11  =  1
nbBus40onTop_12  =  2
nbBus30onTop_5  =  1
nbBus30onTop_6  =  1
nbBus30onTop_7  =  1
nbBus30onTop_9  =  2
nbBus30onTop_10  =  2
nbBus30onTop_11  =  1
objective =  3775.5





"""
