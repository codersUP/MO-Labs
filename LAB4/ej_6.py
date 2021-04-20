import math
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize
from methods import *
from pprint import pprint




#-------F(x)--------------
def F(x):
    n = len(x)
    
    piatoria = 1
    exp_power = 0
    
    for el in x:
        piatoria*= (math.cos(el))
        exp_power-= (el-math.pi)**2
    
    return -1  *  ((-1)**n) * (piatoria) * math.exp(exp_power)   

#--------For x_i <= 500 restrictions-------------
def g_i_1(x_i : float):
    return x_i - 2*math.pi

def g_i_1_plus(x_i : float):
    return max(0,x_i -2* math.pi)
#------For x_i>= -500 restrictions---------------
def g_i_2(x_i : float):
    return -x_i-2*math.pi

def g_i_2_plus(x_i : float):
    return max(0,-x_i-2*math.pi)

#------Q(x,c)-for penalization method----------------

def Q(c):
    def Q_call(x):
        f_x_eval = F(x)
    
        g_i_1_sum = 0
        for variable in x:
            g_i_1_sum +=g_i_1_plus(variable)
        
        g_i_2_sum = 0
        for variable in x:
            g_i_2_sum +=g_i_2_plus(variable)
        
        return f_x_eval + c * g_i_1_sum + c * g_i_2_sum
    
    return Q_call

#------R(x,miu)- for barrier method-------------------
def R(miu):
    def R_call(x):
        f_x_eval = F(x)
        
        g_i_1_sum = 0
        for variable in x:
            g_i_1_sum -=1/g_i_1(variable)
        
        g_i_2_sum = 0
        for variable in x:
            g_i_2_sum -=1/g_i_2(variable)
        
        return f_x_eval + miu * g_i_1_sum + miu * g_i_2_sum
    
    return R_call

#------Omega( chequear si un vector x cumple con las restricciones)-------
def omega(x):
    # print(x)
    for element in x:
        # print(element)
        if element<-2*math.pi or element>2*math.pi:
            return False
    return True




def plot():
    x = np.arange(-2 * math.pi, 2 * math.pi, 0.1);
    y = [F([i]) for i in x]

    plt.plot(x, y)
    plt.show()



#testing-------------------
if __name__ == '__main__':
    plot()

    print("Penalization Method")
    pprint(Penalization_method("BFGS", Q, omega, x0=np.array([3,3]), c0=1, alpha=1.5, epsilon=0.001, k_max=500))
    print()
    print("Barrier Method")
    pprint(Barrier_method("BFGS", R, x0=np.array([3,3]), miu_0=1, alpha=0.5, epsilon=0.000001, k_max=500))