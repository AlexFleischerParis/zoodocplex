from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')

nbbus=nbbus30+nbbus40
mdl.add_kpi(nbbus,"nbbus")
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=True,)

mdl.export("c:\\temp\\buses.lp")

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

for k in mdl.iter_kpis():
    print(k," = ",k.solution_value)

"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0
DecisionKPI(name=nbbus,expr=nbBus40+nbBus30)  =  8.0

"""
