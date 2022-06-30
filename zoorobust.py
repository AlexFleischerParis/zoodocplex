from docplex.mp.model import Model

nbKids=300
nbKidsScenarii=[nbKids+i*10 for i in range(-10,3)]
nbKidsProba=[ 1, 1, 2, 2, 2 ,3 ,3 ,4,  5 ,10 ,50 ,10, 7]
nbScenarii=len(nbKidsScenarii)

assert sum(nbKidsProba)==100

# robust 100%

print("robust 100%")

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
costBus40=500.0;
costBus30=400.0;

nbKidsMax=max(nbKidsScenarii)

ctKid=mdl.add_constraint(nbbus40*40 + nbbus30*30 >= nbKidsMax, 'kids')
mdl.minimize(nbbus40*costBus40 + nbbus30*costBus30)

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("objective = ",mdl.objective_value)

alpha=80; # We want the constraint to be ok with probability 0.80

print()
print("Now robust with probability ",alpha)

mdl.remove_constraints([ctKid])
scenarioIsOk = mdl.binary_var_list(nbScenarii,name="nbBus")

for s in range(0,nbScenarii):
   mdl.add_constraint(scenarioIsOk[s]==(nbbus40*40 + nbbus30*30 >= nbKidsScenarii[s]))

mdl.add_constraint(\
   alpha<=mdl.sum(nbKidsProba[s]*scenarioIsOk[s] \
                  for s in range(0,nbScenarii)))
mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("objective = ",mdl.objective_value)

"""

which gives

robust 100%
nbBus40  =  8.0
nbBus30  =  0
objective =  4000.0

Now robust with probability  80
nbBus40  =  6.0
nbBus30  =  2.0
objective =  3800.0



"""
