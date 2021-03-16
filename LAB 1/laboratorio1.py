from pulp import *

def exercise_1():
    products = ['tomate', 'lechuga', 'acelga']
    P = {'tomate': 80,
         'lechuga': 75,
         'acelga': 86}
    CH = {'tomate': 10,
          'lechuga': 15,
          'acelga': 12}
    H = {'tomate': 5,
         'lechuga': 8,
         'acelga': 7}
    CT = {'tomate': 2,
          'lechuga': 1.5,
          'acelga': 1}

    prob = LpProblem("Problem_1", LpMinimize)
    X = LpVariable.dicts("Product",products,0)

    prob += lpSum([-(X[i] * CH[i] * CT[i] * P[i]) - (X[i] * P[i]) - (X[i] * CH[i] * H[i] * 5) for i in products])

    prob += lpSum([X[i] * CH[i] for i in products]) <= 1200
    prob += lpSum([H[i] for i in products]) <= 450

    prob.solve()
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Total Cost = ", -value(prob.objective))

def main():
    exercise_1()
    

if __name__ == '__main__':
    main()
    