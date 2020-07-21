import random
import math


#number of random draws
n=10000000

#random points in the square of size 1
x=[random.uniform(0, 1) for i in range(0,n)]
y=[random.uniform(0, 1) for i in range(0,n)]

#how many are closer than distance 1 from origin (0,0) ?
nb=sum ([(x[i]*x[i]+y[i]*y[i]<=1) for i in range(0,n)])

#PI from math
print("PI = ",math.pi)
#PI computed as the ratio of number of points within the circle
#   and the total number of points
print("Monte Carlo = ",nb*4/n) 

"""

gives

PI =  3.141592653589793
Monte Carlo =  3.141698

"""
