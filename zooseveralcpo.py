
from docplex.cp.model import CpoModel

mdl = CpoModel(name='buses')

nbbus40 = mdl.integer_var(0,6,name='nbBus40')
nbbus30 = mdl.integer_var(0,6,name='nbBus30')
cost= mdl.integer_var(0,1000000,name='cost')

mdl.add(cost==nbbus40*500 + nbbus30*400)
mdl.add(cost<=4000)
mdl.add(nbbus40*40 + nbbus30*30 >= 300)

siter = mdl.start_search(SearchType='DepthFirst', Workers=1, TimeLimit=100)
# Parameters needed to avoid duplicate solutions



for msol in siter:
    print(msol[nbbus40]," buses 40 seats")
    print(msol[nbbus30]," buses 30 seats")
    print("cost = ",msol[cost])
    
    print("\n")

"""

which gives

3  buses 40 seats
6  buses 30 seats
cost =  3900


 *                      3  0.01s                  4  = nbBus40
4  buses 40 seats
5  buses 30 seats
cost =  4000


 *                      4  0.01s                  4 != nbBus40
6  buses 40 seats
2  buses 30 seats
cost =  3800

"""
