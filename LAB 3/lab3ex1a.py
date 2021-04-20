from itertools import chain,combinations
from sympy import *
import numpy as np
from utils import kkt_condition



def main():
    vector_size =2
    grad_f = lambda x : (-2*x[0], 6*x[1])
    grad_g = [
        lambda x: (2, -2*x[1]),
        lambda x: (-1,0),
        lambda x: (0,-1)
    ]
    grad_h =[]

    ineq = [
        lambda x : 2*x[0]-x[1]**2,
        lambda x : -x[0],
        lambda x : -x[1]
    ]

    pto_x1= (1.5,2.5)
    pto_x2= (0,1)
    pto_x3= (2.75,3.25)

    print(kkt_condition(vector_size,grad_f,grad_h,grad_g,pto_x1,ineq))
    print(kkt_condition(vector_size,grad_f,grad_h,grad_g,pto_x2,ineq))
    print(kkt_condition(vector_size,grad_f,grad_h,grad_g,pto_x3,ineq))

main()