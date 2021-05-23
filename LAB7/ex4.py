from mip import Model, MAXIMIZE, CBC, INTEGER
import time

def solve():
    m = Model(sense=MAXIMIZE, solver_name=CBC)
    
    # Variables
    x1 = m.add_var(var_type=INTEGER, lb=0)
    x2 = m.add_var(var_type=INTEGER, lb=0)
    x3 = m.add_var(var_type=INTEGER, lb=0)

    # Constraints
    m += 3 * x1 + 2 * x2 <= 10
    m += x1 + 4 * x2 <= 11
    m += 3 * x1 + 3 * x2 + x3 == 13

    # Objective function
    m.objective = 4 * x1 + 5 * x2 + x3

    start = time.time()
    status = m.optimize()
    end = time.time()

    print(status)
    print(f'Solution to the objective function: {m.objective_value}')
    print(f'x1: {x1.x}')
    print(f'x2: {x2.x}')
    print(f'x3: {x3.x}')
    print(f'Execution time: {end - start}')


solve()

# OptimizationStatus.OPTIMAL
# Solution to the objective function: 19.0
# x1: 2.0
# x2: 2.0
# x3: 1.0
# Execution time: 0.015565633773803711