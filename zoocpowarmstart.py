from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')
nbbus40 = mdl.integer_var(0,1000,name='nbBus40')
nbbus30 = mdl.integer_var(0,1000,name='nbBus30')
mdl.add(nbbus40*40 + nbbus30*30 >= 300)
mdl.minimize(nbbus40*500 + nbbus30*400)

sol=mdl.create_empty_solution()
sol[nbbus40]=8
sol[nbbus30]=0

mdl.set_starting_point(sol)
msol=mdl.solve()

print(msol[nbbus40]," buses 40 seats")
print(msol[nbbus30]," buses 30 seats") 

"""

which gives

!
 ! Starting point is complete and consistent with constraints.
 *          4000        0  0.01s        1      (gap is 100.0%)
            4000        0          2    1            -
 + New bound is 3800 (gap is 5.00%)
 *          3800        0  0.01s        1      (gap is 0.00%)
 ! ----------------------------------------------------------------------------
 ! Search completed, 2 solutions found.
 ! Best objective         : 3800 (optimal - effective tol. is 0)
 ! Best bound             : 3800

6  buses 40 seats
2  buses 30 seats

"""
