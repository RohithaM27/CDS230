#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:55:33 2024

@author: rohitha_matwada
"""
"""
Name: Rohitha
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


"""
Problem 1
"""
print("\n",40*"-","\n","Problem 9.1:\n",40*"-")

# set constants
k = 1
m = 1

# time step and simulation length
dt = 0.1  # integration time step
t_final = 100

# Set the number of iterations (or simulation length) to be used in the for loop
N = int(t_final / dt)
print('Simulation length: ', N, ' time steps')

# make arrays to store data
t = np.arange(0, t_final, dt)
x = np.zeros(N)
v = np.zeros(N)

# set initial conditions - these are also model parameters
x[0] = -2.0
v[0] = 0
print(f"At time t = {0}, x0 = {x[0]:.2f}, v0 = {v[0]:.2f}")


# Function to compute friction coefficient kd based on position x
def friction_coefficient(x):
    if x < 0.25:
        return 0.1  # low friction, e.g., ice
    elif 0.25 <= x <= 0.5:
        return 1.2  # high friction, e.g., sandpaper
    else:
        return 0.1  # low friction, e.g., ice


# evolve (or integrate), i.e., find solutions
for i in range(1, N):
    kd = friction_coefficient(x[i - 1])
    a = -k * x[i - 1] / m - kd * v[i - 1] / m  # Corrected calculation of acceleration
    v[i] = v[i - 1] + a * dt
    x[i] = x[i - 1] + v[i] * dt

print(f"At time t = {t_final}, state = (x = {x[-1]:.2f}, v = {v[-1]:.2f})")

# Quick visualization
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs. Time')
plt.grid()
plt.show()

plt.plot(x, v)
plt.xlabel('Position (m)')
plt.ylabel('Velocity (m/s)')
plt.title('Phase Space Plot')
plt.grid()
plt.show()


"""
Problem 2
"""
print("\n",40*"-","\n","Problem 9.2:\n",40*"-")

from lotka_volterra import LotkaVolterra

def main():
    # Part a
    sys1 = LotkaVolterra(params=[1, 0.1, 0.5, 0.02], dt=0.1, t_max=50, x0=25, y0=10)
    sys1.update()
    sys1.visualize()

    # Part b
    sys2 = LotkaVolterra(params=[1, 0.1, 0.5, 0.02], dt=0.1, t_max=50, x0=25, y0=10)
    sys2.update(amp=0.1)  # Adding noise
    sys2.visualize()

main()


#explain the differences in the evolution of the populations between part(a) and part(b).
print("In the simulation without noise, the prey population follows a smooth and predictable trajectory over time, maintaining a relatively stable growth pattern. However, in the simulation with added noise, the prey population exhibits fluctuations around its expected trajectory, reflecting the unpredictability introduced by environmental variability. The graphs tends to look very shaky.")
print()
# part d
print("c) Decreasing the dt time step in the Euler method helps reduce body oscillations. Smaller steps increase the accuracy of the equation equation and reduce the number of inconsistencies.")

# part b - USING ODIENT

def Lotka_Volterra(state, t, a, b, c, d):
    x = state[0]
    y = state[1]
    dxdt = a * x - b * x * y
    dydt = -c * y + d * x * y
    return [dxdt, dydt]

t = np.arange(0, 80, 0.1)
x0 = [1000, 100]
a, b, c, d = 0.2, 0.001, 0.5, 0.001

state = odeint(Lotka_Volterra, x0, t, args=(a, b, c, d))

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].plot(t, state[:, 0], 'r', label='rabbits')
ax[0].plot(t, state[:, 1], 'b', label='foxes')
ax[0].set_ylim(ymin=0)
ax[0].set_xlim(xmin=0)
ax[0].set_xlabel('t')
ax[0].set_ylabel('populations')
ax[0].legend()
ax[0].grid()
ax[1].plot(state[:, 0], state[:, 1], 'ks', markersize=2)
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_title('rabbit-foxes phase space')
ax[1].grid()

plt.show()

print("Upon running the simulation with increased time steps, the spring comes to rest after approximately 13.76 seconds. This means that it takes the spring approximately 13.76 seconds to stop oscillating and reach a state where the position oscillations are less than 0.01 m.")

print()

print("The phase space plot looks like a spiral that moves towards the center. This happens because friction slows down the spring's movement, making it lose energy until it stops. So, the plot shows how the spring's speed and position decrease over time until it comes to a rest at the center.")

"""
Problem 3
"""
print("\n",40*"-","\n","Problem 9.3:\n",40*"-")

"""
When using numerical methods like Euler's method to solve the 
differential equation for the simple spring model, there are a few
important practical considerations to keep in mind.
First, the size of the time step used in the numerical method 
can significantly impact the accuracy and stability of the 
solution - smaller time steps generally provide more accurate results,
but require more computational effort.
Second, the initial position and velocity of the mass attached
to the spring need to be specified accurately, as these initial
conditions can greatly influence the solution, especially over longer
simulation times.
The method's accuracy depends on the choice of time step, with smaller
steps generally providing more accurate results but requiring more 
computational resources.

"""

"""
Problem 4 
"""
print("\n",40*"-","\n","Problem 9.4:\n",40*"-")

"""
The simple spring model and the predator-prey models
are both referred to as coupled models becuase two 
or more variables or components in these models are interrelated
or interdependent in the system.

They are called coupling or coupled models becuase changes in
one varaible affectes the other variable in the given system.

In the simple spring model, the position and velocity of the
mass are interrelated through the force exerted by the spring,
while in the predator-prey model, the populations of predators
and prey influence each other's growth rates. 
"""