from docplex.mp.model import Model

# original model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

#now 350 kids instead of 300

print()
print("now 350 kids instead of 300")    
    
mdl.get_constraint_by_name("kids").rhs=350;
mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

# no more than 4 buses 40 seats

print()
print("no more than 4 buses 40 seats")


mdl.get_var_by_name("nbBus40").ub=4
mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

#change the objective so that cost for 40 seats is 450
#and remove the limit on the number of buses 40 seats

print()
print("change the objective so that cost for 40 seats is 450")
print("and remove the limit on the number of buses 40 seats  ")  
    
mdl.get_var_by_name("nbBus40").ub=1000
mdl.set_objective("min",nbbus40*450 + nbbus30*400);
mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0

now 350 kids instead of 300
nbBus40  =  8.0
nbBus30  =  1.0

no more than 4 buses 40 seats
nbBus40  =  2.0
nbBus30  =  9.0

change the objective so that cost for 40 seats is 450
and remove the limit on the number of buses 40 seats  
nbBus40  =  8.0
nbBus30  =  1.0

"""

    
