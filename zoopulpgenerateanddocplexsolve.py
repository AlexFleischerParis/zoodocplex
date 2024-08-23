
# generate a cplex model with pilp
# and solve the model through docplex
# which provides more cplex features
import pulp

bus_problem = pulp.LpProblem("bus", pulp.LpMinimize)

nbBus40 = pulp.LpVariable('nbBus40', lowBound=0, cat='Integer')
nbBus30 = pulp.LpVariable('nbBus30', lowBound=0, cat='Integer')

# Objective function
bus_problem += 500 * nbBus40 + 400 * nbBus30, "cost"

# Constraints
bus_problem += 40 * nbBus40 + 30 * nbBus30 >= 300

bus_problem.writeMPS('c:/temp/model.mps')

from docplex.mp.model import Model
from docplex.mp.model_reader import ModelReader

mdl = Model(name='buses')

mdl = ModelReader.read('c:/temp/model.mps', ignore_names=False)

mdl.solve(log_output=True,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

"""
gives

nbBus30  =  2.0
nbBus40  =  6.0

"""