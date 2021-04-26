from docplex.mp.model import Model

# Now suppose we can rent only 0,1,3,4 or 5 buses of 40 seats buses

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

allowedQuantities=[0,1,3,4,5];
mdl.add_constraint(1==mdl.sum((a==nbbus40) for a in allowedQuantities))

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)


"""

which gives

nbBus40  =  3.0
nbBus30  =  6.0

"""
