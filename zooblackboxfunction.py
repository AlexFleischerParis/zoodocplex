

from docplex.cp.model import *
import docplex.cp.solver.solver as solver
import math

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,10,name='nbBus40')
nbbus30 = mdl.integer_var(0,10,name='nbBus30')
mdl.add(nbbus40*40 + nbbus30*30 >= 300)

#non linear objective
#mdl.minimize(mdl.exponent(nbbus40)*500 + mdl.exponent(nbbus30)*400)

#works fine but let us do the same with black box function
#that are much more flexible since you can run any code

def cost(nbbus40,nbbus30):
    return math.exp(nbbus40)*500+math.exp(nbbus30)*400

cost_bbx = CpoBlackboxFunction(cost)

mdl.minimize(cost_bbx(nbbus40,nbbus30))

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 


"""

which gives

4  buses 40 seats
5  buses 30 seats

"""
