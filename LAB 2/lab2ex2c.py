from gekko import GEKKO
m = GEKKO() # Initialize gekko
m.options.SOLVER=1  # APOPT is an MINLP solver
m.options.IMODE = 5
# optional solver settings with APOPT
m.solver_options = ['minlp_maximum_iterations 500', \
                    # minlp iterations with integer solution
                    'minlp_max_iter_with_int_sol 10', \
                    # treat minlp as nlp
                    'minlp_as_nlp 0', \
                    # nlp sub-problem max iterations
                    'nlp_maximum_iterations 50', \
                    # 1 = depth first, 2 = breadth first
                    'minlp_branch_method 1', \
                    # maximum deviation from whole number
                    'minlp_integer_tol 0.05', \
                    # covergence tolerance
                    'minlp_gap_tol 0.01']

# Initialize variables
x0 = m.Var(value=5,lb=-100000,ub=100000,integer=True)
x1 = m.Var(value=1,lb=-100000,ub=100000,integer=True)
# Equations
m.Equation(3*x0 + 2*x1<=17)
m.Equation(x0**2+x1**2<=100)
m.Equation(x0**2-2*x1<=80)

m.Obj(4*(x1**2)-  x0**3) # Objective
m.solve(disp=True) # Solve
print('Results')
print('x0: ' + str(x0.value))
print('x1: ' + str(x1.value))
print('Objective: ' + str(m.options.objfcnval))