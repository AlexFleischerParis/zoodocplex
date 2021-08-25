from docplex.mp.model import Model

mdl = Model(name='buses')

nbbus50 = mdl.integer_var(name='nbBus50')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')

cost = mdl.continuous_var(name='cost')
co2emission = mdl.continuous_var(name='co2emission')

mdl.add_constraint(nbbus50*50+nbbus40*40 + nbbus30*30 >= 200, 'kids')
mdl.add_constraint(co2emission==nbbus50+nbbus40*1.1+nbbus30*1.2)
mdl.add_constraint(cost==nbbus40*500 + nbbus30*400+nbbus50*625)
                
sense="min"
exprs=[cost,co2emission]
priorities=[1,2]
weights=[1,1]
timelimits=[5, 10]

mdl.set_multi_objective(sense, exprs, priorities, weights, abstols=None,
                        reltols=None, names=None)

mdl.solve(lex_mipgaps = [0.001, 0.05], log_output=True,lex_timelimits = timelimits)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("The minimum cost is ",cost.solution_value);
print("CO2 emission is ",co2emission.solution_value);

'''
which gives

nbBus50  =  4.0
nbBus40  =  0
nbBus30  =  0
The minimum cost is  2500.0
CO2 emission is  4.0

'''
