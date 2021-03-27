import sympy as sp
from numpy.linalg import matrix_rank
from itertools import chain,combinations


def kkt_condition(vector_size,grad_f,  grad_h, grad_g, x, ineq_constraints):

    active_index_gradients = active_indexes(x,ineq_constraints,grad_g)
    
    matrix = []
    for grad in [*grad_h, *active_index_gradients]:
        row = [grad(x)[i] for i in range(len(x))]
        matrix.append(row)

    LICQ = matrix_rank(matrix) == len(grad_h) + len(active_index_gradients)
        

    lambdas = sp.symbols("l0:%d" % len(grad_h))
    mius = sp.symbols("m0:%d" % len(active_index_gradients))

    
    linear_system = equation_system(x,vector_size, lambdas,mius,grad_f,grad_h,active_index_gradients)


    solutions = sp.solve(linear_system, [*lambdas, *mius])
    mius_sol = solutions[len(lambdas) :]

    if len(solutions) != 0:
        if LICQ:
            return all(i >= 0 for i in mius_sol) 
        else:
            return True
    
    return False  

def active_indexes(x,ineq_g,grad_g):
    active_gi =[]
    for i in range(len(ineq_g)):
        if not ineq_g[i](x):
            active_gi.append(grad_g[i])
    return active_gi

def equation_system(x,vector_size ,lambdas,mius,grad_f,grad_h,active_g):
    
    equ_system=[]
    for i in range(vector_size):
        equation = grad_f(x)[i]
        for j, grad in enumerate(grad_h):
            equation += lambdas[j] * grad(x)[i]

        for j, grad in enumerate(active_g):
            equation += mius[j] * grad(x)[i]

        equ_system.append(sp.Eq(equation, 0))

    return equ_system

