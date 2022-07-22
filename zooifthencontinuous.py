from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.continuous_var(name='nbBus40')
nbbus30 = mdl.continuous_var(name='nbBus30')
lessthan3buses40 = mdl.binary_var(name='lessthan3buses40')

mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 600, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_continuous_vars():
   print(v," = ",v.solution_value)

print()
print("with if nb buses 40 more than 3  then nbBuses30 more than 7")

#if then constraint

#mdl.add(mdl.if_then(nbbus40>=3,nbbus30>=7))
# nbbus40>=30 is not discrete so that should be rewritten

mdl.add_indicator(lessthan3buses40,nbbus40<=2,active_value = 1)
mdl.add(mdl.if_then(lessthan3buses40==0,nbbus30>=7))

    
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_continuous_vars():
    print(v," = ",v.solution_value)

 """

gives

nbBus40  =  15.0
nbBus30  =  0

with if nb buses 40 more than 3  then nbBuses30 more than 7
nbBus40  =  9.75
nbBus30  =  7.0

"""
