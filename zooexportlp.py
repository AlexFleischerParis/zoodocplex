from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)



mdl.export("c:\\temp\\buses.lp")




"""

which gives in buses.lp

Minimize
 obj: 500 nbBus40 + 400 nbBus30
Subject To
 kids: 40 nbBus40 + 30 nbBus30 >= 300

Bounds

Generals
 nbBus40 nbBus30
End




"""
