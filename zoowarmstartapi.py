from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

warmstart=mdl.new_solution()
warmstart.add_var_value(nbbus40,8)
warmstart.add_var_value(nbbus30,0)
mdl.add_mip_start(warmstart)


sol=mdl.solve(log_output=True)

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

'''

which gives

nbBus40  =  6.0
nbBus30  =  2.0

and in the log we see

1 of 1 MIP starts provided solutions.
MIP start 'm1' defined initial solution with objective 4000.0000.




'''
