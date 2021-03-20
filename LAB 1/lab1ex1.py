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

    prob += -lpSum([(P[i] * CT[i] * X[i] - X[i] * P[i] / CH[i] - X[i] * H[i] * 5) for i in products])

    prob += lpSum([X[i] for i in products]) <= 1200
    prob += lpSum([X[i] * H[i] for i in products]) <= 450

    for p in products:
        prob += X[p] >= 0

    prob.solve()
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Ganancias = ", -value(prob.objective))


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

    prob += -lpSum([X[a][b] * G[a] for (a, b) in Dist])

    for (a, b) in Dist:
        prob += X[a][b] >= 0

    for a in articulos:
        prob += lpSum([X[a][b] for b in bodegas]) <= T[a]
    for b in bodegas:
        prob += lpSum([X[a][b] for a in articulos]) <= C[b]
    prob += lpSum([X[a]['proa'] for a in articulos])/C['proa'] == lpSum([X[a]['centro'] for a in articulos])/C['centro'] == lpSum([X[a]['popa'] for a in articulos])/C['popa']

    prob.solve()
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Ganancias = ", -value(prob.objective))


def exercise_3():
    productos = ['P1', 'P2']
    ingredientes = ['M1', 'M2', 'aceite', 'secador', 'solvente']

    P = {'P1': { 'M1': 0,
                 'M2': 0,
                 'aceite': 80,
                 'secador': 10,
                 'solvente': 10},
         'P2': { 'M1': 0, 
                 'M2': 0, 
                 'aceite': 55, 
                 'secador': 15, 
                 'solvente': 30}}

    CT = {'M1': 500,
          'M2': 150,}

    PR = {'M1': 3.20,
          'M2': 2.20,
          'aceite': 3.80,
          'secador': 2.60,
          'solvente': 1.20}

    CP = {'P1': 550,
          'P2': 420}

    Y = {'M1': { 'M1': 0,
                 'M2': 0,
                 'aceite': 70,
                 'secador': 10,
                 'solvente': 20},
         'M2': { 'M1': 0, 
                 'M2': 0, 
                 'aceite': 40, 
                 'secador': 0, 
                 'solvente': 60},
         'aceite': { 'M1': 0, 
                     'M2': 0, 
                     'aceite': 100, 
                     'secador': 0, 
                     'solvente': 0},
         'secador': { 'M1': 0, 
                      'M2': 0, 
                      'aceite': 0, 
                      'secador': 100, 
                      'solvente': 0},
         'solvente': { 'M1': 0, 
                       'M2': 0, 
                       'aceite': 0, 
                       'secador': 0, 
                       'solvente': 100}}

    prob = LpProblem("Problem_3", LpMinimize)

    Dist = [(i,p) for i in ingredientes for p in productos]

    X = LpVariable.dicts("Cant_de_hl",(ingredientes, productos),0)

    prob += lpSum([X[i][p] * PR[i] for (i, p) in Dist])

    for (i, p) in Dist:
        prob += X[i][p] >= 0

    for i in ['M1', 'M2']:
        prob += lpSum([X[i][p] for p in productos]) <= CT[i]

    for p in productos:
        prob += lpSum([X[i][p] for i in ingredientes]) >= CP[p]

    for p in productos:
        for k in ['aceite', 'secador', 'solvente']:
            print(p, k)
            prob += lpSum([X[i][p] * Y[i][k] for i in ingredientes]) == (P[p][k] * lpSum([X[i][p] for i in ingredientes]))

    prob.solve()
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Ganancias = ", value(prob.objective))

def main():
    # exercise_1()
    # exercise_2()
    exercise_3()
    

if __name__ == '__main__':
    main()
    