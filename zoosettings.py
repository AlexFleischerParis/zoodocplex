from docplex.mp.model import Model

mdl = Model(name='buses')

mdl.parameters.timelimit=20;
mdl.set_time_limit(20) #The same

nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

mdl.export("c:\\temp\\buses.lp")

print("time limit = ",mdl.parameters.timelimit.get())
print("time limit = ",mdl.get_time_limit()) #The same

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

'''

which gives

time limit =  20.0
time limit =  20.0
nbBus40  =  6.0
nbBus30  =  2.0


'''
