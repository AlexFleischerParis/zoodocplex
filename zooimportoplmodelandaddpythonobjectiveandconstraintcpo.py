"""

Here from docplex we call an OPL model
without any objective
that will generate a .cpo filr
that we read in docplex and then
we add an objective and a new constraint and
then we solve

"""


from docplex.cp.model import CpoModel
from doopl.factory import *

# Create an OPL model from a .mod file
with create_opl_model(model="zoooplwithoutobjectivecpo.mod") as opl:
    # Generate the problem and solve it.
    opl.run()

mdl = CpoModel(name='buses')

mdl.import_model("zoowithoutobj.cpo")

vars=mdl.get_all_variables()

for i in vars:
    print(i.name)
    if (i.name=="nbBus40"):
        nbbus40=i
    if (i.name=="nbBus30"):
        nbbus30=i

#add docplex constraint        
mdl.add(nbbus40<=4)
#add docplex objective
mdl.minimize(nbbus40*500 + nbbus30*400)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats")

"""

which gives

3  buses 40 seats
6  buses 30 seats

"""


    
