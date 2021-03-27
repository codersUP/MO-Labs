import numpy as np

from scipy.optimize import minimize



def rosen(x):

    """The Rosenbrock function"""

    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)



def exercise_2(n:int):
    # x0 = np.array([0 for i in range(n)])
    x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2]) # Este es el de la documentación
    # x0 = np.array([20, 12, 57, 9, 76])
    

    res = minimize(rosen, x0, method='nelder-mead',

               options={'xatol': 1e-8, 'disp': True})
    print(res.x)

exercise_2(5)

