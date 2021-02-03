from docplex.mp.model import Model

# a bus has a size and a cost
class Bus:
    def __init__(self, size, cost):
        self.size = size
        self.cost = cost

    def __repr__(self):
        return f"Bus(size={self.size},cost={self.cost})"

# a school has nbKids kids
class School:
    def __init__(self, nbKids):
        self.nb_kids = nbKids
        self.buses = []
        self._nb_buses = None

    def add_bus_kind(self, b):
        self.buses.append(b)
        # clear cached number of buses
        self._nb_buses = None

    def optimize_buses(self):
        print(f"-- The school has to transport {self.nb_kids} kids")
        for b in self.buses:
            print(f"--A bus with size {b.size} costs {b.cost}")
        with Model('buses') as mdl:
            # decision variables
            bus_vars = mdl.integer_var_dict(self.buses, name="nbBus")
            # use function version of scalar product, aka dotf
            def bus_size(bus_):
                # a local function to compute bus size, to be used in Model.dotf below
                return bus_.size

            mdl.add_constraint(mdl.dotf(bus_vars, bus_size) >= self.nb_kids, 'kids')

            # a local function to compute bus cost
            def bus_cost(bus_):
                # a local function to compute bus size, to be used in Model.dotf below
                return bus_.cost
            mdl.minimize(mdl.dotf(bus_vars, bus_cost))

            sol = mdl.solve(log_output=True)
          
            if sol:
                self._nb_buses = sol.get_value_dict(bus_vars)
            else:
                self._nb_buses = {bus: 0 for bus in self.buses}

    @property
    def nb_buses(self):
        if self._nb_buses is None:
            # need to recompute number of buses, only once
            print(f"-- optimizing number of buses")
            self.optimize_buses()
            assert self._nb_buses is not None
        return self._nb_buses

    def display(self):
        n_buses = self.nb_buses  # use lazy property: optimize on demand
        for b in n_buses:
            print(f"-- {n_buses[b]} buses with {b.size} seats")

# 300 kids
myschool = School(300)
# 40 seats
bus40 = Bus(40, 500)
# 30 seats
bus30 = Bus(30, 400)
myschool.add_bus_kind(bus40)
myschool.add_bus_kind(bus30)
print(myschool.nb_buses)
# no re-optimization needed here
myschool.display()

"""

which gives

-- 6.0 buses with 40 seats
-- 2.0 buses with 30 seats
"""
