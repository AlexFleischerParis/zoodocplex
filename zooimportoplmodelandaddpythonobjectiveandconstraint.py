"""

Here from docplex we call an OPL model
without any objective
that will generate a .lp file
that we read in docplex and then
we add an objective and a new constraint and
then we solve

"""


from docplex.mp.model import Model
from docplex.mp.model_reader import ModelReader
from doopl.factory import *

# Create an OPL model from a .mod file
with create_opl_model(model="zoooplwithoutobjective.mod") as opl:
    # Generate the problem and solve it.
    opl.run()

mdl = ModelReader.read_model('zoowithoutobj.lp', model_name='zoo')

nbbus40 = mdl.find_matching_vars('nbBus40')[0]
nbbus30 = mdl.find_matching_vars('nbBus30')[0]

#add docplex constraint        
mdl.add(nbbus40<=4)
#add docplex objective
mdl.minimize(nbbus40*500 + nbbus30*400)

msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats")

"""

which gives

3.0  buses 40 seats
6.0  buses 30 seats

"""


    
