from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
nbbusvars=[nbbus40,nbbus30]

mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 200, 'kids')

#all : all quantities should be less than 5
for nb in nbbusvars:
    mdl.add(nb<=5)

#any : one of the quantities should be 4
mdl.add(1<=(mdl.sum(nb==1 for nb in nbbusvars)))    

mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=True,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

#asserts with all and any

assert all(nb.solution_value<=5 for nb in nbbusvars)    
assert any(nb.solution_value==1 for nb in nbbusvars)  

"""

which gives

nbBus40  =  5.0
nbBus30  =  1.0

"""
