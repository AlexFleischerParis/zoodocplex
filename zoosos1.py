from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

print("and with SOS1")

mdl.add_sos1([nbbus40,nbbus30])

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)


"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0
and with SOS1
nbBus40  =  8.0
nbBus30  =  0

"""
