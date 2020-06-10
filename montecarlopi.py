

import random
import math

n=10000000
x=[random.uniform(0, 1) for i in range(0,n)]
y=[random.uniform(0, 1) for i in range(0,n)]

nb=sum ([(x[i]*x[i]+y[i]*y[i]<=1) for i in range(0,n)])

print("PI = ",math.pi)
print("Monte Carlo = ",nb*4/n) 

"""

gives

PI =  3.141592653589793
Monte Carlo =  3.141698

"""
