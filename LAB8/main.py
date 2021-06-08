from viajante import viajante_ants
from MIP_CBC import solve_CBC, generate_distance_matrix
import matplotlib.pyplot as plt
import numpy as np

def main():

    ants_times =[]
    ants_results =[]

    mip_times =[]
    mip_results =[]
    x_axes= [i for i in range(2,15)]
    

    for i in range(2,15):
        distances = generate_distance_matrix(i)
        path, solver, colony = viajante_ants(np.array(distances))

        duration_ants = solver.plugins['Timer'].duration
        ants_times.append(duration_ants)
        ants_results.append(path.cost)

        result, time =solve_CBC(i,distances)
        mip_times.append(time)
        mip_results.append(result)
    
    plt.plot(x_axes, ants_times,label="Ants")
    plt.xlabel("Number of cities.")
    plt.ylabel("Time taken to solve (seconds).")
    plt.plot(x_axes ,mip_times, label= "CBC")
    plt.legend()
    plt.show()

    plt.plot(x_axes, ants_results,label="Ants")
    plt.xlabel("Number of cities.")
    plt.ylabel("Costs.")
    plt.plot(x_axes ,mip_results, label= "CBC")
    plt.legend()
    plt.show()

main()

