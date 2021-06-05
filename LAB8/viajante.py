import acopy
import networkx as nx
import numpy as np
from acopy.utils.plot import Plotter
from random import randint

def generate_travels(n):
    ret = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        for j in range(i + 1, n):
            ret[i][j] = ret[j][i] = randint(1, 100)
    return ret
            

def viajante_ants(matrix,rho=.03,q=1,alpha=1,beta=3):
    G = nx.Graph(matrix)
    solver = acopy.Solver(rho=rho, q=q)
    colony = acopy.Colony(alpha=alpha, beta=beta)
    
    solver.add_plugin(acopy.plugins.Printout())
    solver.add_plugin(acopy.plugins.Timer())
    solver.add_plugin(acopy.plugins.StatsRecorder())
    
    path = solver.solve(G, colony, limit=100)
    
    t = solver.plugins['Timer']
    print('Time per iter:')
    print(t.time_per_iter)
    print('Duration:')
    print(t.duration)
    
    return (path, solver, colony)


# costs = np.array(generate_travels(5))
prices = [[0, 22, 11, 4],
          [22, 0, 8, 5],
          [11, 8, 0, 4],
          [4, 5, 4, 0]]
costs = np.array(prices)
path, solver, colony = viajante_ants(costs)

print(solver)
Plotter(solver.plugins['StatsRecorder'].stats).plot()