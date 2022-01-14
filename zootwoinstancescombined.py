from docplex.mp.model import Model

#Two independent schools, first school 300 kids, second one 350
#Combined in a single model because of a coupling constraint
#(Total number of buses)

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
nbbus40bis = mdl.integer_var(name='nbBus40bis')
nbbus30bis = mdl.integer_var(name='nbBus30bis')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.add_constraint(nbbus40bis*40 + nbbus30bis*30 >= 350, 'kids2')
mdl.add_constraint(nbbus40+nbbus30+nbbus40bis+nbbus30bis<=17,'total nb of buses')
mdl.minimize(nbbus40*500 + nbbus30*400+nbbus40bis*500 + nbbus30bis*400)

mdl.solve(log_output=True,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)


"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0
nbBus40bis  =  8.0
nbBus30bis  =  1.0

"""
