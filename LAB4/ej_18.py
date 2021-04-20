from scipy import optimize
import numpy as np
from matplotlib import pyplot as plt
import math
from methods import *
from pprint import pprint

def F(x):
    return (4 - 2.1*x[0]**2 + 1/3*x[0]**4)*x[0]**2 + x[0]*x[1] + 4 * (x[1]**2 - 1) * x[1]**2

def g_1_plus(x):
    return max(0, x - 3)
def g_2_plus(x):
    return max(0, -3 - x)
def g_3_plus(x):
    return max(0, x - 2)
def g_4_plus(x):
    return max(0, -2 - x)

def g_1(x):
    return  x - 3
def g_2(x):
    return  -3 - x
def g_3(x):
    return x - 2
def g_4(x):
    return -2 - x


def Q(c):
    def Q_call(x):
        f_x_eval = F(x)
    
        eval_cond = []

        eval_cond.append(g_1_plus(x[0]))
        eval_cond.append(g_2_plus(x[0]))
        eval_cond.append(g_3_plus(x[1]))
        eval_cond.append(g_4_plus(x[1]))
        
        sum = 0
        for i in eval_cond:
            sum += i

        return f_x_eval + c * sum
    
    return Q_call


def R(miu):
    def R_call(x):
        f_x_eval = F(x)
        
        eval_cond = []

        eval_cond.append(g_1(x[0]))
        eval_cond.append(g_2(x[0]))
        eval_cond.append(g_3(x[1]))
        eval_cond.append(g_4(x[1]))
        
        sum = 0
        for i in eval_cond:
            sum += i

        
        return f_x_eval + miu * sum
    
    return R_call


def omega(x):
    if x[0] >= -3 and x[0] <= 3 and x[1] >= -2 and x[1] <= 2:
            return True
    return False

def plot():
    x_v = np.arange(-3, 3, 0.01)
    y_v = np.arange(-2, 2, 0.01)

    x = []
    y = []
    z = []
    for i in x_v:
        for j in y_v:
            x.append(i)
            y.append(j)
            z.append(F([i, j]))

    plt.scatter(x, y, c=z)
    plt.show()

if __name__ == '__main__':
    plot()
    
    print("Penalization Method")
    pprint(Penalization_method("BFGS", Q, omega, x0=np.array([-1,-1]), c0=1, alpha=1.5, epsilon=0.001, k_max=500))
    print()
    print("Barrier Method")
    pprint(Barrier_method("BFGS", R, x0=np.array([1,1]), miu_0=1, alpha=0.9, epsilon=0.001, k_max=500))