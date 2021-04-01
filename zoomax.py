from docplex.mp.model import Model

mdl = Model(name='buses')

nbKids=300;
buses=[30,40,50]

#decision variables
mdl.nbBus = {b: mdl.integer_var(name="nbBus"+str(b)) for b in buses}

# Constraint
mdl.add_constraint(sum(mdl.nbBus[b]*b for b in buses) >= nbKids, 'kids')

# Objective
mdl.minimize(mdl.max(mdl.nbBus[b] for b in buses)) 

mdl.solve(log_output=True,)

mdl.export("c:\\temp\\buses.lp")

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

   


"""

which can give

nbBus30  =  3.0
nbBus40  =  3.0
nbBus50  =  2.0

"""
