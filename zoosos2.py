from docplex.mp.model import Model

mdl = Model(name='buses')

nbbus30 = mdl.integer_var(name='nbBus30')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus50 = mdl.integer_var(name='nbBus50')

cost = mdl.continuous_var(name='cost')


mdl.add_constraint(nbbus50*50+nbbus40*40 + nbbus30*30 >= 300, 'kids')

mdl.add_constraint(cost==nbbus40*500 + nbbus30*400+nbbus50*550)
mdl.add_constraint(nbbus50==1)

mdl.minimize(cost)
                
mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("The minimum cost is ",cost.solution_value);    

print("and then with sos2   nbbus30,nbbus40,nbbus50")



mdl.add_sos2([nbbus30,nbbus40,nbbus50])

mdl.minimize(cost)
                
mdl.solve( )

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("The minimum cost is ",cost.solution_value);


'''
which gives

nbBus30  =  3.0
nbBus40  =  4.0
nbBus50  =  1.0
The minimum cost is  3750.0
and then with sos2   nbbus30,nbbus40,nbbus50
nbBus30  =  0
nbBus40  =  7.0
nbBus50  =  1.0
The minimum cost is  4050.0

'''
