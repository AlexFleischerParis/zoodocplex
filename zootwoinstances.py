from docplex.mp.model import Model

#Two independent schools, first school 300 kids, second one 350

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=True,)

mdlbis = Model(name='busesbis')
nbbus40bis = mdlbis.integer_var(name='nbBus40bis')
nbbus30bis = mdlbis.integer_var(name='nbBus30bis')
mdlbis.add_constraint(nbbus40bis*40 + nbbus30bis*30 >= 350, 'kids')
mdlbis.minimize(nbbus40bis*500 + nbbus30bis*400)

mdlbis.solve(log_output=True,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

for v in mdlbis.iter_integer_vars():
    print(v," = ",v.solution_value)


"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0
nbBus40bis  =  8.0
nbBus30bis  =  1.0

"""
