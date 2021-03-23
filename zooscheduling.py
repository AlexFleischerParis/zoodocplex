"""

Model written by Philippe Laborie

https://www.linkedin.com/pulse/zoo-buses-kids-optimization-resource-allocation-philippe-laborie/

"""

# u('08:30') -> 510
def u(hhmm):
  (h,m) = hhmm.split(':')
  result = int(h) * 60 + int(m)
  return result

# s(510) -> 08:30
def s(v):
  result = str(v // 60).zfill(2) + ':' + str(v % 60).zfill(2)
  return result

import collections as col

Bus = col.namedtuple('Bus', 'Name, Seats, Cost, Avail, Outward, Return')

Buses = [
  Bus('A40', 40,   500,  u('08:00'),  u('00:30'), u('00:25')),
  Bus('B40', 40,   500,  u('08:00'),  u('00:30'), u('00:25')),
  Bus('C40', 40,   500,  u('08:00'),  u('00:30'), u('00:25')),
  Bus('D40', 40,   500,  u('08:00'),  u('00:30'), u('00:25')),
  Bus('E40', 40,   500,  u('08:30'),  u('00:30'), u('00:25')),
  Bus('F30', 30,   400,  u('08:00'),  u('00:25'), u('00:20')),
  Bus('G30', 30,   400,  u('08:00'),  u('00:25'), u('00:20')),
  Bus('H30', 30,   400,  u('08:00'),  u('00:25'), u('00:20')),
  Bus('I30', 30,   400,  u('08:00'),  u('00:25'), u('00:20')),
  Bus('J30', 30,   400,  u('08:30'),  u('00:25'), u('00:20'))
]

Opening    = u('10:00')
NbKids     = 300
NbTeachers = 3
NbMaxTrips = 2
NbBuses    = len(Buses)

from docplex.cp.model import *

# Create model object
model = CpoModel()

# Create decision interval variables
outwardTrip = [[interval_var(optional = True,
                             size  = Buses[b].Outward,
                             start = [Buses[b].Avail, Opening],
                             end   = [Buses[b].Avail, Opening]) for i in range(NbMaxTrips)] for b in range(NbBuses)]

roundTrip   = [[interval_var(optional = True,
                             size  = Buses[b].Outward + Buses[b].Return) for i in range(NbMaxTrips)] for b in range(NbBuses)]

# Minimize total cost
model.add(minimize(sum(presence_of(outwardTrip[b][i]) * Buses[b].Cost for b in range(NbBuses) for i in range(NbMaxTrips))))

# Schedule enough buses to transport all the kids
model.add(NbKids <= sum(presence_of(outwardTrip[b][i]) * Buses[b].Seats for b in range(NbBuses) for i in range(NbMaxTrips)))

# Limited availability for teachers given that each roundtrip requires one teacher
model.add(sum(pulse(roundTrip[b][i],1) for b in range(NbBuses) for i in range(NbMaxTrips)) <= NbTeachers);

for b in range(NbBuses):
    for i in range(NbMaxTrips):
        # Intervals outwardTrip and roundTrip have same presence status and start at the same time
        model.add(presence_of(outwardTrip[b][i]) == presence_of(roundTrip[b][i]))
        model.add(start_at_start(outwardTrip[b][i], roundTrip[b][i]))
        if 0<i:
            # If we perform round trip #i it means that we have performed round trip #i-1 before
            model.add(presence_of(roundTrip[b][i]) <= presence_of(roundTrip[b][i-1]))
            model.add(end_before_start(roundTrip[b][i-1],roundTrip[b][i]))



# Solve the model
sol = model.solve(LogPeriod=1000000,trace_log=True)

import datetime
import docplex.cp.utils_visu as visu
import matplotlib.pyplot as plt

from pylab import rcParams
rcParams['figure.figsize'] = 15, 3

now = datetime.datetime.now().strftime("%Y-%m-%d ")

df = [
    dict(Task     = Buses[b].Name, 
         Start    = now + s(sol.get_var_solution(outwardTrip[b][i]).start),
         Finish   = now + s(sol.get_var_solution(outwardTrip[b][i]).end), 
         Seats    = str(Buses[b].Seats) + " Seats")
    for b in range(NbBuses) for i in range(NbMaxTrips) if (sol.get_var_solution(outwardTrip[b][i]).is_present())
]

for i in df:
  print(i)

visu.timeline('Buses')
visu.panel(name="Schedule")
for b in range(NbBuses):
  for i in range(NbMaxTrips):
    if (sol.get_var_solution(outwardTrip[b][i]).is_present()):
        visu.interval(sol.get_var_solution(outwardTrip[b][i]), int(Buses[b].Seats), sol.get_var_solution(outwardTrip[b][i]).length)
visu.show()        

"""

which gives

{'Task': 'A40', 'Start': '2021-03-22 09:30', 'Finish': '2021-03-22 10:00', 'Seats': '40 Seats'}
{'Task': 'D40', 'Start': '2021-03-22 09:30', 'Finish': '2021-03-22 10:00', 'Seats': '40 Seats'}
{'Task': 'E40', 'Start': '2021-03-22 09:30', 'Finish': '2021-03-22 10:00', 'Seats': '40 Seats'}
{'Task': 'F30', 'Start': '2021-03-22 08:45', 'Finish': '2021-03-22 09:10', 'Seats': '30 Seats'}
{'Task': 'G30', 'Start': '2021-03-22 08:00', 'Finish': '2021-03-22 08:25', 'Seats': '30 Seats'}
{'Task': 'H30', 'Start': '2021-03-22 08:00', 'Finish': '2021-03-22 08:25', 'Seats': '30 Seats'}
{'Task': 'I30', 'Start': '2021-03-22 08:00', 'Finish': '2021-03-22 08:25', 'Seats': '30 Seats'}
{'Task': 'I30', 'Start': '2021-03-22 08:45', 'Finish': '2021-03-22 09:10', 'Seats': '30 Seats'}
{'Task': 'J30', 'Start': '2021-03-22 08:45', 'Finish': '2021-03-22 09:10', 'Seats': '30 Seats'}

"""
