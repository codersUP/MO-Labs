 
from mip import *
import time
from random import randint



def solve_CBC(n , d_i_j):
    m = Model(solver_name=CBC)
    
    # Variables
    delta_i_j_k = [[[m.add_var(var_type= BINARY) for i in range(n)] for j in range(n)] for k in range(n)]

    # Constraints
    m+= xsum(delta_i_j_k[0][i][0] for i in range(n)) == 1

    for k in range(1,n):
        m+= xsum(delta_i_j_k[i][j][k] for i in range(n) for j in range(n)) == 1

    for i in range(n):
        m+= xsum(delta_i_j_k[i][j][k] for j in range(n) for k in range(n)) == 1

    for j in range(n):
        for k in range(n-1):
            m+= xsum(delta_i_j_k[i][j][k] for i in range(n)) - xsum(delta_i_j_k[j][i][k+1] for i in range(n)) == 0

    m+= xsum(delta_i_j_k[i][0][n-1] for i in range(n)) == 1


    # Objective function
    m.objective = xsum(delta_i_j_k[i][j][k] * d_i_j[i][j] for i in range(n) for j in range(n) for k in range(n))

    start = time.time()
    status = m.optimize()
    end = time.time()

    print()
    print(status)
    print(f'Solution to the objective function: {m.objective_value}')
    print(f'Execution time: {end - start}')

    print(f'\nJourney:')
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if delta_i_j_k[i][j][k].x:
                    print(f"{i} -> {j}")


def generate_distance_matrix(n: int):
    dists = [[0]*n for _ in range(n)] 
    for i in range(n):
        for j in range(i + 1, n):
            dists[i][j] = dists[j][i] = randint(1, 100)
    return dists


dimension = 5
distances = generate_distance_matrix(5)

solve_CBC(dimension,distances)



