from gekko import GEKKO
m = GEKKO(remote=False) # Initialize gekko
m.options.SOLVER=1  # APOPT is an MINLP solver
# m.options.IMODE = 5
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
x0 = m.Var(value=5,lb=0,integer=True)
x1 = m.Var(value=1,lb=0,integer=True)
# Equations
m.Equation(3*x0 + 2*x1<=50)
m.Equation(2*x0+x1<=30)
m.Obj(3*x1-x0**2) # Objective
m.solve(disp=True) # Solve
print('Results')
print('x1: ' + str(x0.value))
print('x2: ' + str(x1.value))
print('Objective: ' + str(m.options.objfcnval))