from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
#mdl.add_constraint(285<=(nbbus40*40 + nbbus30*30) , 'kids')
#mdl.add_constraint((nbbus40*40 + nbbus30*30) <= 290, 'kids2')
mdl.add_range(285,(nbbus40*40 + nbbus30*30),290,"kids")
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=True,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

"""

which gives

nbBus40  =  5.0
nbBus30  =  3.0

"""
