"""
Name: Rohitha
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""
Problem 1
"""
print("\n",40*"-","\n","Problem 8.1:\n",40*"-")
# refer to discrete1.py
"""
Problem 2
"""
print("\n",40*"-","\n","Problem 8.2:\n",40*"-")
# Parameters (constants)
r = 0.01  # growth rate
# Initialization
x0 = 8
K = 10
N = 76
print('Simulation length:',N)

t_dif = np.arange(N)
x_dif = np.zeros(N)

# evaluate difference equation (logistic growth)
x_dif[0] = x0
for j in t_dif[1:]:
    x_dif[j] = x_dif[j-1] + x_dif[j-1]* r *(1-x_dif[j-1]/K)  # add carrying capacity limit K (new parameter)

# visualize
fig, ax = plt.subplots()
ax.axhline(K, color = 'r', linestyle ='--', label = 'Carrying Capacity')
ax.plot(t_dif + 2024, x_dif, '+', label = 'Numerical solution')
ax.set_xlabel('Year')
ax.set_ylabel('Population (billion)')
ax.set_title('World Population Growth (2024 - 2100)')
ax.legend()
ax.grid()
#_ = ax.set_xlim([2024, 2100])

# Calculate Numerical solution at t=76 (2100)
print(f"Numerical solution for population at 2100: {x_dif[-1]:.2f} billion")

# Calculate analytical solution at t=76 (2100)
analytical_population_2100 = K * (1 + ((K - x0)/ x0)) * np.exp(-r * N)
print(f"Analytical solution for population at 2100: {analytical_population_2100:.2f} billion")
print()

print("Will the world reach the carrying capacity by the end of the century?")
print()
print("Accordign to the graph I have plot, by the year 2100, the world population doesn't really reach the carrying capacity. However, if I were to plot the graph over a longer period (let's say may be until 2500 years or so), the world population will most likely reach the carrying capacity. My explanation is definitely validated by the information shown on the the given website as well. According to the website the world population will reach k at 2058 or later.")
print()
print("When comparing the logistical growth model(Numerical solution) with the analytical solution, I see that the world population numbers are different. Logistical growth model is a approximation of the scenario, so it may not accurateky represent the actual population growth, but it gives a good approximation to predict the future numberes. ")
"""
Problem 3
"""
print("\n",40*"-","\n","Problem 8.3:\n",40*"-")
# Parameters
#r = 0.1 # or r = -0.1 (decay)

# Initialization
y0 = -2
t_start = 0
t_final = 5
#dt = 1

t = np.linspace(t_start, t_final, 100)

# compute solution using SciPy ODEINT package
def exp_model(y, t):
    dydt = (y-2)**2
    return dydt
 
y = odeint(exp_model, y0, t)

# visualize
fig, ax = plt.subplots()
ax.plot(t, y, 'r', label = 'y(t)' )
ax.grid()
ax.legend()
plt.show()
_ = ax.set_xlim([0, t_final-1])

