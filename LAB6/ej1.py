import numpy as np

from scipy.optimize import linprog


def ex1():
    c = np.array([-2, -3])
    A = np.array([[1, 1], [1, 2], [-1, 1]])
    b = np.array([3, 4, 1])

    x1_bounds = (0, None)
    x2_bounds = (0, None)

    res = linprog(c, A, b, bounds=(x1_bounds, x2_bounds), method='simplex')
    print("Ex1")
    print(res)

def ex4():
    A = np.array([[1, -1], [-4, 1]])
    b = np.array([1, 4])
    
    c_a = np.array([1, 0])
    c_b = np.array([-2, 1])
    c_c = np.array([8, -2])

    x1_bounds = (0, None)
    x2_bounds = (0, None)

    res_a = linprog(c_a, A, b, bounds=(x1_bounds, x2_bounds), method='simplex')
    res_b = linprog(c_b, A, b, bounds=(x1_bounds, x2_bounds), method='simplex')
    res_c = linprog(c_c, A, b, bounds=(x1_bounds, x2_bounds), method='simplex')
    
    print("Ex4a")
    print(res_a)
    print("Ex4b")
    print(res_b)
    print("Ex4c")
    print(res_c)


def ex5():
    c = np.array([1, 1, 4])
    A = np.array([[1, -1, -1], [2, -3, -3]])
    b = np.array([1, 2])

    x1_bounds = (0, None)
    x2_bounds = (0, None)
    x3_bounds = (0, None)

    res = linprog(c, A_eq=A, b_eq=b, bounds=(x1_bounds, x2_bounds, x3_bounds), method='simplex')
    print("Ex5")
    print(res)

def ex6():
    c = np.array([1, 2])

    A_eq= np.array([[2, -5]])
    b_eq = np.array([4])

    x1_bounds = (0, None)
    x2_bounds = (0, None)
    
    A = np.array([[-1, 2]])
    b = np.array([-6])

    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=(x1_bounds, x2_bounds), method='simplex')
    print("Ex6 a = 2")
    print(res)

    A = np.array([[-1, 3]])
    b = np.array([-6])

    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=(x1_bounds, x2_bounds), method='simplex')
    print("Ex6 a = 3")
    print(res)

ex1()
ex4()
ex5()
ex6()
