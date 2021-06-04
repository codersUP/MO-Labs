from mip import Model, MAXIMIZE, CBC, INTEGER
import time

def solve():
    m = Model(solver_name=CBC)
    
    # Variables
    x1 = m.add_var(var_type=INTEGER, lb=0)
    x2 = m.add_var(var_type=INTEGER, lb=0)
    x3 = m.add_var(var_type=INTEGER, lb=0)

    # Constraints
    m += 2 * x1 - 3 * x2  + 3 * x3 <= 4
    m += 4 * x1 + x2  + x3 <= 8

    # Objective function
    m.objective = -2 * x1 - x2 - x3

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
# Solution to the objective function: -8.0
# x1: 0.0
# x2: 8.0
# x3: 0.0
# Execution time: 0.5075554847717285