"""
Name: Rohitha
"""
import numpy as np
import matplotlib.pyplot as plt
"""
Problem 1
"""
print("\n",40*"-","\n","Problem 8.1:\n",40*"-")

def initialize(data, init_cond):
    """ 
    Set up the initial values for all the state variables of the system 
    data is an uninitialized array
    init_cond is a floating point value that represents the IC of the system
    """
    data[0] = init_cond
    return data

def update(data, nsteps, growth_factor, b ):
    """ Update state variables for geometric growth system"""
    for k in range(1, nsteps):
        data[k] = growth_factor*data[k-1]+b
    return data

def observe(data, k=0):
    """ Monitor the state of the system (printing the state)"""
    if k:
        print(f'Data: ({data[k]:.2f})')
        return
    else:
        print(f'Data: ({data[0]:.2f})')

def visualize(data, ax, title):
    """ Visualize system state """
    ax.plot(data)
    ax.set_title(title)
    

def main():
    
    # model parameters
    a_b = [(1.05, 0.0), (0.95, 0.0), (1.05, 1.0), (1.05, -1.0)]
    #num_cases = len(a_b)
   
    # initial condition
    init_val = 1
    # size of data
    N = 30
    
    #Plotting
    fig,ax = plt.subplots(2,2, figsize = (12,10))
    
    for i in range(0, 2):
        for j in range(0, 2):
            my_data = np.zeros(N)
            my_data = initialize(my_data, init_val)
            observe(my_data, k=0)
            my_data = update(my_data, N, a_b[i*2+j][0], a_b[i*2+j][1])
            visualize(my_data, ax[i, j], f'a={a_b[i*2+j][0]}, b={a_b[i*2+j][1]}')
    
    plt.tight_layout()
   
main()


