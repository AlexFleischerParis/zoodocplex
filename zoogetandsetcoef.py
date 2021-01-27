from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
ctKids=mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve(log_output=False,)


for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)


for v in ctKids.iter_variables():
   print(v," --> ",ctKids.lhs.get_coef(v))

#And now let us allow 5 more kids per bus
print("And now let us allow 5 more kids per bus")

for v in ctKids.iter_variables():  
   ctKids.lhs.add_term(v,5)


for v in ctKids.iter_variables():
   print(v," --> ",ctKids.lhs[v])

mdl.solve(log_output=False,)


for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)

'''

which gives

nbBus40  =  6.0
nbBus30  =  2.0
nbBus40  -->  40
nbBus30  -->  30
And now let us allow 5 more kids per bus
nbBus40  -->  45
nbBus30  -->  35
nbBus40  =  6.0
nbBus30  =  1.0

'''



