from docplex.mp.model import Model
from docplex.mp.progress import *

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

class pl(ProgressListener):
  
    def __init__(self):
        ProgressListener.__init__(self, ProgressClock.Gap)
    
    def notify_progress(self, pdata):
        gap = pdata.mip_gap
        ms_time = 1000* pdata.time
        print('-- new gap: {0:.1%}, time: {1:.0f} ms'.format(gap, ms_time))
        

# connect a listener to the model
mdl.add_progress_listener(pl())

mdl.solve(log_output=False,)

mdl.export("c:\\temp\\buses.lp")

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)


"""

which gives

-- new gap: 6.2%, time: 31 ms
-- new gap: 3.8%, time: 78 ms
nbBus40  =  6.0
nbBus30  =  2.0

"""
