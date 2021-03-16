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

    prob += -lpSum([(X[i] * CH[i] * CT[i] * P[i]) - (X[i] * P[i]) - (X[i] * CH[i] * H[i] * 5) for i in products])

    prob += lpSum([X[i] * CH[i] for i in products]) <= 1200
    prob += lpSum([H[i] for i in products]) <= 450

    prob.solve()
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Total Cost = ", -value(prob.objective))


def exercise_2():
    bodegas = ['proa', 'centro', 'popa']
    articulos = ['A', 'B', 'C']

    T = {'A': 6000,
         'B': 4000,
         'C': 2000}
    
    C = {'proa': 2000,
         'centro': 3000,
         'popa': 1500}

    G = {'A': 6,
         'B': 8,
         'C': 5}

    prob = LpProblem("Problem_2", LpMinimize)

    Dist = [(a,b) for a in articulos for b in bodegas]

    X = LpVariable.dicts("Product",(articulos, bodegas),0)

    prob += lpSum([-X[a][b] * G[a] for (a, b) in Dist])

    for a in articulos:
        prob += lpSum([X[a][b] for b in bodegas]) <= T[a]
    for b in bodegas:
        prob += lpSum([X[a][b] for a in articulos]) <= C[b]
    prob += lpSum([X[a]['proa'] for a in articulos])/C['proa'] == lpSum([X[a]['centro'] for a in articulos])/C['centro'] == lpSum([X[a]['popa'] for a in articulos])/C['popa']

    prob.solve()
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Maxime = ", -value(prob.objective))


def main():
    exercise_1()
    exercise_2()
    

if __name__ == '__main__':
    main()
    