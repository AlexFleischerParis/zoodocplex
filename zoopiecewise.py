'''

let s now deal with a new information : for a given bus size
if we take more than 4 then we get a 20% discount

This moves our function cost from linear to piecewise linear.

'''

from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')

#after 4 buses, additional buses of a given size are cheaper
f=mdl.piecewise(0, [(0, 0),(4,4)], 0.8)

mdl.minimize(f(nbbus40)*500 + f(nbbus30)*400)

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

'''

which gives

nbBus40  =  0
nbBus30  =  10.0

'''
