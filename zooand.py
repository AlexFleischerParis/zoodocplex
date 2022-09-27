from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_integer_vars():
   print(v," = ",v.solution_value)

print()
print("with nb buses 40 less than 3 and nb buses 30  more than 7")

option1=mdl.binary_var(name='option1')
option2=mdl.binary_var(name='option2')

mdl.add(option1==(nbbus40<=3))
mdl.add(option2==(nbbus30>=7))

mdl.add(1==mdl.logical_and(option1,option2))

mdl.minimize(nbbus40*500 + nbbus30*400)

mdl.solve()

for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)
