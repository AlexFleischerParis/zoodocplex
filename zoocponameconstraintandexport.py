import numpy as np
np.bool = np.bool_

from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')

nbKidsConstraint = (nbbus40*40 + nbbus30*30 >= 300)
nbKidsConstraint.set_name("nbKids")
mdl.add(nbKidsConstraint)
mdl.export_model("c:/temp/zoo.cpo")
mdl.minimize(nbbus40*500 + nbbus30*400)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 


"""

which gives

6  buses 40 seats
2  buses 30 seats

and in zoo.cpo

//--- Constants ---

//--- Variables ---
#line 12 "c:/GitHub/zoodocplex/zoocponameconstraintandexport.py"
nbBus40 = intVar(0..1000);
nbBus30 = intVar(0..1000);

//--- Expressions ---
#line 12 "c:/GitHub/zoodocplex/zoocponameconstraintandexport.py"
nbKids: nbBus40 * 40 + nbBus30 * 30 >= 300;

"""
