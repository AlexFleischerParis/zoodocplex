"""
For some models solution pool does not work so here let's see
how to manage without solution pools
"""

from docplex.mp.model import Model


mdl = Model(name='buses')
nbbus40 = mdl.integer_var(name='nbBus40')
nbbus30 = mdl.integer_var(name='nbBus30')
mdl.add_constraint(nbbus40*40 + nbbus30*30 >= 300, 'kids')
mdl.minimize(nbbus40**2*500 + nbbus30**2*400)

nb_iter=5

for iter in range(0,nb_iter):
    mdl.solve()
    nbbus40sol=int(nbbus40.solution_value)
    nbbus30sol=int(nbbus30.solution_value)
    print(int(nbbus40sol)," buses 40 seats")
    print(int(nbbus30sol)," buses 30 seats")
    print("cost : ",mdl.objective_value)
    print()
    mdl.add_constraint(mdl.logical_or((nbbus40sol!=nbbus40),
            nbbus30sol!=nbbus30))


"""

which gives

4  buses 40 seats
5  buses 30 seats
cost :  18000.0

5  buses 40 seats
4  buses 30 seats
cost :  18900.0

3  buses 40 seats
6  buses 30 seats
cost :  18900.0

6  buses 40 seats
2  buses 30 seats
cost :  19600.0

6  buses 40 seats
3  buses 30 seats
cost :  21600.0

"""
