
# generate a cplex model with pyomo
# and solve the model through docplex
# which provides more cplex features
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

opt = pyo.SolverFactory("cplex")

opt.options['mip limits solutions'] = 1

model = pyo.ConcreteModel()

model.nbBus = pyo.Var([40,30], domain=pyo.PositiveIntegers)

model.OBJ = pyo.Objective(expr = 500*model.nbBus[40] + 400*model.nbBus[30])

model.Constraint1 = pyo.Constraint(expr = 40*model.nbBus[40] + 30*model.nbBus[30] >= 300)

#opt.solve(model) # this would solve through pyomo

model.write("c:/temp/model.mps",io_options = {"symbolic_solver_labels":True})

from docplex.mp.model import Model
from docplex.mp.model_reader import ModelReader

mdl = Model(name='buses')

mdl = ModelReader.read('c:/temp/model.mps', ignore_names=False)

mdl.solve(log_output=True,)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

"""
gives

nbBus(30)  =  2.0
nbBus(40)  =  6.0

"""