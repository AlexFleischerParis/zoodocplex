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
with create_opl_model(model="zoooplschedulingwithoutobjective.mod") as opl:
    # Generate the problem and solve it.
    opl.run()

mdl = CpoModel(name='buses')

mdl.import_model("zoooplschedulingwithoutobj.cpo")

vars=mdl.get_all_variables()

bus40=[]
bus30=[]

for i in vars:
    print(i.name)
    if ("roundTrip" in i.name) and ("500" in i.name):
        bus40.append(i)
    if ("roundTrip" in i.name) and ("400" in i.name):
        bus30.append(i)


#add docplex objective
mdl.minimize(500*sum(mdl.presence_of(b40) for b40 in bus40)  +\
             400*sum(mdl.presence_of(b30) for b30 in bus30))

msol=mdl.solve()

print("objective = ",msol.get_objective_values()[0])
print()

for i in bus40:
    if msol.get_var_solution(i).is_present():
        print(i)

for i in bus30:
    if msol.get_var_solution(i).is_present():
        print(i)

"""

which gives

objective =  3900

"roundTrip({\"E40\",40,500,510,30,25})(1)" = intervalVar(optional, size=55)
"roundTrip({\"D40\",40,500,480,30,25})(1)" = intervalVar(optional, size=55)
"roundTrip({\"A40\",40,500,480,30,25})(1)" = intervalVar(optional, size=55)
"roundTrip({\"J30\",30,400,510,25,20})(1)" = intervalVar(optional, size=45)
"roundTrip({\"I30\",30,400,480,25,20})(2)" = intervalVar(optional, size=45)
"roundTrip({\"I30\",30,400,480,25,20})(1)" = intervalVar(optional, size=45)
"roundTrip({\"H30\",30,400,480,25,20})(1)" = intervalVar(optional, size=45)
"roundTrip({\"G30\",30,400,480,25,20})(1)" = intervalVar(optional, size=45)
"roundTrip({\"F30\",30,400,480,25,20})(1)" = intervalVar(optional, size=45)

"""


    
