from docplex.mp.model import Model

mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40*500 + nbbus30*400)
mdl.solve(log_output=True,)

#display solution
for v in mdl.iter_integer_vars():
    print(v," = ",v.solution_value)
print(mdl.print_solution())    

#write solution to a file
f= open("c://temp//sol.txt", "w")
for v in mdl.iter_integer_vars():
    f.write(str(v)+" = "+str(v.solution_value)+'\n')
print(type(print(mdl.print_solution())))    
f.close()

#option 2

mdl.solution.export("zoosolution.json")

#option 3

with open("zoosolution.txt", "w") as solfile:
    solfile.write(mdl.solution.to_string())

"""

which gives

nbBus40  =  6.0
nbBus30  =  2.0

in the display and in the file sol.txt

and in zoosolution.txt

solution for: buses
objective: 3800
nbBus40=6
nbBus30=2


"""
