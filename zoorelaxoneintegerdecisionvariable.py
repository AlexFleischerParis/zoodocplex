from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=False,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

nbbus30.set_vartype('C')

print("relax nbbus30 to continuous")

mdl.solve(log_output=False,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)
for v in mdl.iter_continuous_vars():
    print(v," = ",v.solution_value)

print("set  nbbus30 back to integer")

nbbus30.set_vartype('I')

mdl.solve(log_output=False,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0
relax nbbus30 to continuous
nbBus40  =  7.0
nbBus30  =  0.6666666666666666
set  nbbus30 back to integer
nbBus40  =  6.0
nbBus30  =  2.0

"""
