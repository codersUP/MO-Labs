import numpy as np
import math
import copy
from scipy import optimize
import time

def NewtonMethod(f, der_f, second_der_f, xk, k):
    der_f_x = der_f(xk)

    # print(xk, k, der_f_x)

    if np.isclose(VectorNorm(der_f_x), 0):
        return (xk, k)

    inverse_second_der = second_der_f(xk).getI()

    k1 = k + 1
    xk1 = xk - (inverse_second_der * der_f_x).transpose()


    return NewtonMethod(f, der_f, second_der_f, xk1, k1)


def BFGSMehtod(f, der_f, xk, Sk, tk, k):
    gk = der_f(xk)

    if np.isclose(VectorNorm(gk), 0):
        return (xk, k)

    m1 = 0.1
    m2 = 0.9

    tk = GoldsteinRule(xk, f, der_f, m1, m2, tk)

    xk1 = xk - (tk * Sk * gk).transpose()

    pk = xk1 - xk
    pk = pk.transpose()

    gk1 = der_f(xk1)
    qk = gk1 - gk

    second = (1 + ((qk.transpose() * Sk * qk) / (pk.transpose() * qk))).getA()[0][0] * ((pk * pk.transpose())/(pk.transpose() * qk))
    therd = ((pk*qk.transpose()*Sk + Sk*qk*pk.transpose())/(pk.transpose()*qk))

    # second = (pk * pk.transpose())/(pk.transpose()*qk)
    # therd = (Sk*qk*qk.transpose()*Sk)/(qk.transpose()*Sk*qk)
    Sk1 = Sk + second - therd

    k1 = k + 1

    return BFGSMehtod(f, der_f, xk1, Sk1, tk, k1)


def CalculateStep(xk, f, der_f, m1, m2, t, tg, td, a, b, c, h, derH):
    print(t, tg, td)
    if a(xk, f, der_f, m1, m2, t, h, derH):
        return t
    if b(xk, f, der_f, m1, m2, t, h, derH):
        td = t
    elif c(xk, f, der_f, m1, m2, t, h, derH):
        tg = t


    if np.isclose(td, 0):
        t = 10 * tg
        print(t, tg, td)
        return CalculateStep(xk, f, der_f, m1, m2, t, tg, td, a, b, c, h, derH)
    t = (td + tg) / 2
    print(t, tg, td)
    return CalculateStep(xk, f, der_f, m1, m2, t, tg, td, a, b, c, h, derH)


def DerH(xk, der_f, t, dk):
    if np.isclose(t, 0):
        return der_f(xk).transpose() * dk    

    return der_f(xk + (t * dk).transpose()).transpose() * dk
    

def H(xk, f, t, dk):
    return f(xk + (t * dk)) - f(xk)


def ACritery(xk, f, der_f, m1, m2, t, h, der_h):
    dk = -1 * der_f(xk)
    ht = h(xk, f, t, dk)

    return ((m2 * der_h(xk, der_f, 0, dk) * t) <= ht) and (ht <= (m1 * der_h(xk, der_f, 0, dk) * t))

def BCritery(xk, f, der_f, m1, m2, t, h, der_h):
    dk = -1 * der_f(xk)
    ht = h(xk, f, t, dk)

    return ht > (m1 * der_h(xk, der_f, 0, dk) * t)

def CCritery(xk, f, der_f, m1, m2, t, h, der_h):
    dk = -1 * der_f(xk)
    ht = h(xk, f, t, dk)

    return ht < (m2 * der_h(xk, der_f, 0, dk) * t)


def GoldsteinRule(xk, f, der_f, m1, m2, t):
    return CalculateStep(xk, f, der_f, m1, m2, t, 0, 0, ACritery, BCritery, CCritery, H, DerH)
    
    
def VectorNorm(x):
    result = 0

    for i in x:
        result += i[0]**2
    
    return math.sqrt(result)


def Penalization_method(Irrestricted_method, Q_method, omega,x0,c0, alpha,epsilon, k_max):
    start = time.time()
    total_irrestricted_iterations =0      
    total_irrestricted_time =0
    
    c = c0
    k=0    
    
    x_k = None   
    x_k1 = x0

    it = 0
    norm = epsilon +1 
    while norm > epsilon and k < k_max:

        aux1 =copy.deepcopy(x_k1)
        
        Q_x_c = Q_method(c)

        minimize_time_start = time.time()
        result = optimize.minimize(Q_x_c, x_k1,method=Irrestricted_method)
        minimize_time_end = time.time()
        
        x_k1 = result.x
        total_irrestricted_iterations+=result.nit
        total_irrestricted_time+= minimize_time_end-minimize_time_start

        x_k =aux1        

        norm = np.linalg.norm([x_k[i] - x_k1[i] for i in range(len(x_k1))])
        
        it+=1
        if(omega(x_k1)):
            continue
        else:
            c = alpha *c            
            k+=1
    
    total_time = time.time() - start
    answer = {"0.  x0" : x0,
              "1.Result" : x_k1, 
              "2.Time" : total_time, 
              "3.Iteraciones/ Cantidad de llamados a metodo irrestricto" : it,
              "4.Cantidad total de iteraciones de metodo irrestricto" : total_irrestricted_iterations,
              "5.Promedio de iteraciones de metodo irrestricto" : total_irrestricted_iterations/it,
              "6.Promedio de tiempo de metodo irrestricto" : total_irrestricted_time/it 
              }
    return answer

def Barrier_method(Irrestricted_method, R_method, x0,miu_0, alpha,epsilon, k_max):
    start = time.time()
    
    total_irrestricted_iterations =0      
    total_irrestricted_time =0
    
    miu = miu_0
    k=0    
    
    x_k = None    
    x_k1 = x0


    norm = epsilon +1 
    while norm > epsilon and k < k_max:

        aux1 =copy.deepcopy(x_k1)
        
        R_x_miu = R_method(miu)

        minimize_time_start = time.time()
        result=  optimize.minimize(R_x_miu, x_k1, method=Irrestricted_method)
        minimize_time_end = time.time()

        x_k1 = result.x
        total_irrestricted_iterations+=result.nit
        total_irrestricted_time+= minimize_time_end-minimize_time_start
        
        x_k =aux1 
    
        miu = alpha *miu        
        k+=1

        norm = np.linalg.norm([x_k[i] - x_k1[i] for i in range(len(x_k1))])
    
    total_time = time.time() - start
    answer = {"0.   x0" :x0,
              "1.Result" : x_k1, 
              "2.Time" : total_time, 
              "3.Iteraciones/ Cantidad de llamados a metodo irrestricto" : k,
              "4.Cantidad total de iteraciones de metodo irrestricto" : total_irrestricted_iterations,
              "5.Promedio de iteraciones de metodo irrestricto" : total_irrestricted_iterations/k,
              "6.Promedio de tiempo de metodo irrestricto" : total_irrestricted_time/k 
              }
    return answer