from viajante import viajante_ants
from MIP_CBC import solve_CBC, generate_distance_matrix
import matplotlib.pyplot as plt

def main():

    ants_results =[]
    mip_result =[]
    

    for i in range(2,20):
        distances = generate_distance_matrix(i)
        path, solver, colony = viajante_ants(distances)

        duration_ants = solver.plugins['Timer'].duration
        ants_results.append((i,duration_ants))

        result, time =solve_CBC(i,distances)
        mip_result.append((i,time))
    
    plt.plot(ants_results,label="Ants")
    plt.plot(mip_result, label= "CBC")
    plt.legend()
    plt.show()

main()

