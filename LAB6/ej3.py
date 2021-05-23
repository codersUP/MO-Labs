import numpy as np
from scipy.optimize import linprog

def ej3():
    C = np.array([-3/4, 20, -1/2, 6])

    A_ub = np.array([[1/4, -8, -1, 9],
                     [1/2, -12, -1/2, 3],
                     [0, 0, 1, 0]])
    b_ub = np.array([0, 0, 1])

    x1_bounds = (0, None)
    x2_bounds = (0, None)
    x3_bounds = (0, None)
    x4_bounds = (0, None)    

    bounds = [x1_bounds, x2_bounds, x3_bounds, x4_bounds]

    result = linprog(C, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='simplex')
    print(result)

if __name__ == '__main__':
    ej3()