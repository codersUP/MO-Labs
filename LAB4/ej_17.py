import math
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize
from methods import *


def FirstDerivateSchwefelsFunction(x):
    result = []

    x_list = x.getA()[0]

    for i in x_list:
        result.append(-(math.sin(math.sqrt(abs(i))) + (i**2*math.cos(math.sqrt(abs(i)))) / (2 * math.sqrt(abs(i)**3))))

    return np.matrix([[x] for x in result])


def SecondDerivateSchwefelsFunction(x):
    x_list = x.getA()[0]

    result = [[0 for i in range(len(x_list))] for j in range(len(x_list))]

    for ind, i in enumerate(x_list):
        result[ind][ind] = ((i*math.pow(abs(i), 7/2)*math.sin(math.sqrt(abs(i)))-3*i**3*abs(i)*math.cos(math.sqrt(abs(i)))) / (4*math.pow(abs(i), 9/2)))

    return np.matrix(result)


#-------F(x)--------------
def F(x):
    result = 0

    for i in x:
        result += i * math.sin(math.sqrt(abs(i)))

    return -result

#--------For x_i <= 500 restrictions-------------
def g_i_1(x_i : float):
    return x_i -500

def g_i_1_plus(x_i : float):
    return max(0,x_i -500)
#------For x_i>= -500 restrictions---------------
def g_i_2(x_i : float):
    return -x_i-500

def g_i_2_plus(x_i : float):
    return max(0,-x_i-500)

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
        if element<-500 or element>500:
            return False
    return True




def plot():
    x = np.arange(-500, 500, 0.1)
    y = [F([i]) for i in x]

    plt.plot(x, y)
    plt.show()



#testing-------------------
if __name__ == '__main__':
    plot()

    print(Penalization_method("BFGS", Q, omega, x0=np.array([380,380]), c0=1, alpha=1.5, epsilon=0.001, k_max=500))
    print(Barrier_method("BFGS", R, x0=np.array([380,380]), miu_0=1, alpha=0.5, epsilon=0.001, k_max=500))
    print(SQP_method(F, x0=np.array([380,380]), bounds=[(-500, 500), (-500, 500)], k_max=500))