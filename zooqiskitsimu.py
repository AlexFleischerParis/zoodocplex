from docplex.mp.model import Model

from qiskit import BasicAer
from qiskit.aqua.algorithms import QAOA, NumPyMinimumEigensolver
from qiskit.optimization.algorithms import CobylaOptimizer, MinimumEigenOptimizer
from qiskit.optimization.problems import QuadraticProgram

qaoa = MinimumEigenOptimizer(QAOA(quantum_instance=BasicAer.get_backend('statevector_simulator')))

nbKids=150
costBus40=500
costBus30=400

model = Model()
#nbBus40b2 = model.binary_var(name='nbBus40b2')
nbBus40b1 = model.binary_var(name='nbBus40b1')
nbBus40b0 = model.binary_var(name='nbBus40b0')
#nbBus30b2 = model.binary_var(name='nbBus30b2')
nbBus30b1 = model.binary_var(name='nbBus30b1')
nbBus30b0 = model.binary_var(name='nbBus30b0')

model.minimize(#nbBus40b2*4*costBus40+
               nbBus40b1*2*costBus40+nbBus40b0*costBus40+
               #nbBus30b2*4*costBus30+
               nbBus30b1*2*costBus30+nbBus30b0*costBus30)
model.add_constraint(#nbBus40b2*4*40+
                     nbBus40b1*2*40+nbBus40b0*40+
                     #nbBus30b2*4*30+
                     nbBus30b1*2*30+nbBus30b0*30>=nbKids
                     , "nbKids")

model.solve(log_output=True,)

for v in model.iter_binary_vars():
    print(v," = ",v.solution_value)

obj = model.objective_value
print("obj =",obj)

# load quadratic program from docplex model
qp = QuadraticProgram()
qp.from_docplex(model)
print(qp.export_as_lp_string())

# run QAOA
result = qaoa.solve(qp)

bresult=result.x

print("x={}".format(bresult))
print("fval={:.2f}".format(result.fval))

print()

print("cost = ",result.fval)
solnbbus40=2*bresult[0]+bresult[1]
solnbbus30=2*bresult[2]+bresult[3]

print(solnbbus40, " buses 40 seats and ",solnbbus30, "buses 30 seats")

"""
which gives

cost =  1900.0
3.0  buses 40 seats and  1.0 buses 30 seats

"""

