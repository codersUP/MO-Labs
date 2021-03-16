from pulp import *


def exercise_2():
    encendido = 500

    products = ['gouda', 'edam']

    LP = {'gouda': 2.5,
          'edam': 2}

    PP = {'gouda': 1,
          'edam': 1.5}

    P = {'gouda': 4,
          'edam': 5}

    cant_leche = 2000
    presupuesto = 1500

    prob = LpProblem("Problem_1", LpMinimize)

    X = LpVariable.dicts("Product",products,0, None, LpInteger)
    Y = LpVariable.dicts("FacturyOn", products, 0, 1, LpInteger)

    prob += -lpSum([X[i] * P[i] - X[i] * PP[i] - Y[i] * encendido for i in products])

    prob += lpSum([X[i] * LP[i] for i in products]) <= cant_leche
    prob += lpSum([X[i] * PP[i] + Y[i] * encendido for i in products]) <= presupuesto
    
    for p in products:
        prob += X[p] <= (cant_leche / LP[p]) * Y[p]

    prob.solve()
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Ganancias = ", -value(prob.objective))


def exercise_4():
    dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    cursos = ['1', '2', '3', '4', '5']

    A = {'lunes': {'1': 3,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '5': 9},
         'martes': {'1': 0,
                    '2': 10,
                    '3': 5,
                    '4': 8,
                    '5': 10},
         'miercoles': {'1': 1,
                       '2': 3,
                       '3': 3,
                       '4': 10,
                       '5': 2},
         'jueves': {'1': 6,
                    '2': 1,
                    '3': 1,
                    '4': 0,
                    '5': 5},
         'viernes': {'1': 0,
                     '2': 8,
                     '3': 6,
                     '4': 2,
                     '5': 3},}
    
    prob = LpProblem("Problem_4", LpMinimize)

    Asist = [(d,c) for d in dias for c in cursos]

    X = LpVariable.dicts("Seleccionado",(dias, cursos),0, 1, LpInteger)

    prob += lpSum([X[d][c] * A[d][c] for (d, c) in Asist])

    for c in cursos:
        prob += lpSum([X[d][c] for d in dias]) == 1

    for d in dias:
        prob += lpSum(X[d][c] for c in cursos) == 1

    prob.solve()
    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Pérdida de asistencias total= ", value(prob.objective))


def main():
    exercise_2()
    exercise_4()


if __name__ == '__main__':
    main()