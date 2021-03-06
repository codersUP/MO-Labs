from mip import Model, MAXIMIZE, CBC, INTEGER
import time

def solve():
    m = Model(solver_name=CBC)
    
    # Variables
    x1 = m.add_var(var_type=INTEGER, lb=0)
    x2 = m.add_var(var_type=INTEGER, lb=0)

    # Constraints
    m += 2 * x1 + 2 * x2 == 3
    m += x1 + 2 * x2 <= 2

    # Objective function
    m.objective = x1 + 2 * x2

    start = time.time()
    status = m.optimize()
    end = time.time()

    print(status)
    print(f'Solution to the objective function: {m.objective_value}')
    print(f'x1: {x1.x}')
    print(f'x2: {x2.x}')
    print(f'Execution time: {end - start}')


solve()

# OptimizationStatus.INFEASIBLE
# Solution to the objective function: None
# x1: None
# x2: None
# Execution time: 0.011461734771728516
