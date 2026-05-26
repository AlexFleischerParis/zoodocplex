#!/usr/bin/python
# ---------------------------------------------------------------------------
# File: zoocallOPL.py
# ---------------------------------------------------------------------------
# Zoo transportation problem using OPL model with tuple set
# Reads zootupleset.mod and uses Buses data

import sys
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

try:
    import docplex
    print(f"DOcplex version: {docplex.__version__}")
except Exception as e:
    print(f"Error importing docplex: {e}")
    sys.exit(1)

from docplex.mp.model_reader import ModelReader

# Check if build_opl_model exists
if not hasattr(ModelReader, 'build_opl_model'):
    print("ERROR: ModelReader.build_opl_model not found!")
    print(f"Available methods: {[m for m in dir(ModelReader) if not m.startswith('_')]}")
    sys.exit(1)

try:
    from docplex.util.environment import IndexedSet
except ImportError:
    # Fallback for older versions
    try:
        from docplex.util.collections import IndexedSet
    except ImportError:
        # If neither works, use a simple list of tuples
        IndexedSet = list

# Read the OPL model from file
with open('zootupleset.mod', 'r') as f:
    mod = f.read()


# Buses data: (capacity, cost) -> converted to tuple set with nbSeats and cost
# Buses = [(40, 500), (30, 400)]
Buses = IndexedSet([
    (40, 500),   # Bus type 1: 40 seats, cost 500
    (30, 400)    # Bus type 2: 30 seats, cost 400
])

# Build the model with data
mdl = ModelReader.build_opl_model(
    mod,
    buses=Buses
)

# Solve the model
sol = mdl.solve()

if sol:
    print("=" * 60)
    print("Zoo Transportation Problem - Optimal Solution")
    print("=" * 60)
    print(f"Number of kids to transport: 300")  # nbKids is defined in .mod file
    print(f"Objective Value (Total Cost): ${sol.get_objective_value():.2f}")
    print()
    
    # Extract OPL variables
    all_vars = mdl.get_opl_var()
    all_vars_sol = all_vars.from_solution(sol)
    
    print("Bus Allocation:")
    print("-" * 60)
    for seats in all_vars_sol.nbBus:
        nb_buses = all_vars_sol.nbBus[seats]
        if nb_buses > 0:
            print(f"  {int(nb_buses)} buses with {seats} seats")
    
    print("-" * 60)
    print("=" * 60)
else:
    print("No solution found")

"""
which gives

Number of kids to transport: 300
Objective Value (Total Cost): $3800.00

Bus Allocation:
------------------------------------------------------------
  6 buses with 40 seats
  2 buses with 30 seats
------------------------------------------------------------

"""

# Made with Bob
