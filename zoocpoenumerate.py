

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

from pandas import *
dfsol=pandas.DataFrame()

for msol in siter:
    print(msol[nbbus40]," buses 40 seats")
    print(msol[nbbus30]," buses 30 seats")
    print("cost = ",msol[cost])
    dfsol=concat([dfsol,DataFrame([msol[nbbus40],msol[nbbus30],msol[cost]])],axis=1)
    print("\n")
dfsol.columns=["sol1","sol2","sol3"]


print(dfsol)

"""

which gives

   sol1  sol2  sol3
0     3     4     6
1     6     5     2
2  3900  4000  3800

"""
