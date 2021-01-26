from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=False,)

mdlclone=mdl.clone()
mdlequal=mdl;


# set upper bound for nbbus40 to 0
nbbus40.ub=0

mdlclone.solve(log_output=False,)
mdlequal.solve(log_output=False,)


print("clone")
for v in mdlclone.iter_integer_vars():
    print(v," = ",v.solution_value)

print("= operator")
for v in mdlequal.iter_integer_vars():
    print(v," = ",v.solution_value)

'''

which gives

clone
nbBus40  =  6.0
nbBus30  =  2.0
= operator
nbBus40  =  0
nbBus30  =  10.0

'''



