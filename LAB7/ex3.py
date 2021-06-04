from mip import Model, MAXIMIZE, CBC, INTEGER
import time

def solve():
    m = Model(solver_name=CBC)
    
    # Variables
    x1 = m.add_var(var_type=INTEGER, lb=0)
    x2 = m.add_var(var_type=INTEGER, lb=0)

    # Constraints
    m += 2 * x1 + 3 * x2 == 6
    m += 2 * x1 + 9 * x2 <= 6

    # Objective function
    m.objective = x1 + x2

    start = time.time()
    status = m.optimize()
    end = time.time()

    print(status)
    print(f'Solution to the objective function: {m.objective_value}')
    print(f'x1: {x1.x}')
    print(f'x2: {x2.x}')
    print(f'Execution time: {end - start}')


solve()

# OptimizationStatus.OPTIMAL
# Solution to the objective function: 3.0
# x1: 3.0
# x2: 0.0
# Execution time: 0.013741016387939453