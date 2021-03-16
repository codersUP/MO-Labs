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

    X = LpVariable.dicts("Product",products,0)
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


def main():
    exercise_2()


if __name__ == '__main__':
    main()