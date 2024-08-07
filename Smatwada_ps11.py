#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 00:12:05 2024

@author: rohitha_matwada
"""
import numpy as np
import matplotlib.pyplot as plt
import random

"""
Problem 1
"""
print("\n",40*"-","\n","Problem 11.1 :\n",40*"-")

# define function
def f(x):
    return ( np.exp(-x) / ( 1 + ( x - 1 )**2 ) )

# visualize function
x = np.linspace(0, np.pi*2 , 100)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Plot of z(x)")
ax.set_xlabel("x values")
ax.set_ylabel("z(x)")
ax.grid()

# set MC parameters (limits)
a = 0
b = np.pi*2
N = 10000

xrand = np.random.randint(a, b, N)

# perform one MC integration

# Evaluate f(x) at all x = xrand
my_sum = 0
for i in range(N):
    my_sum += f(xrand[i])

# Estimate area (1 trial). Result will be different each time.
area1 = (b-a)*my_sum/N
print('Approximate area: ',area1)

print()

# Create a distribution of areas
N_areas = 100
# initialize areas
areas = np.zeros(N_areas)

N_rand = 10000  # number of random numbers
# outer loop here
for i in range(N_areas):
    xrand = np.random.uniform(a, b, N_rand)
    my_sum = 0.0
    # loop over xrand numbers
    for j in range(N_rand):
        my_sum += f(xrand[j])
    # aggregate each area
    areas[i] = (b-a)*my_sum/N_rand
    
fig, ax = plt.subplots()
ax.set_title('Distribution of areas');
ax.hist(areas, bins=50, ec='black');
ax.set_ylabel('Number of areas');
ax.set_xlabel('Area values');

areas.mean()
exact_value =0.696092 #what should i plug in for x????
print('Exact value: ',exact_value)
print(f"Absolute error:  {abs(exact_value - areas.mean()):.8f}")

"""
Problem 2
"""
print("\n",40*"-","\n","Problem 11.2:\n",40*"-")


def f(x):
    return np.sqrt(1 - x**2)

def error(S, n):
    x = np.random.uniform(0, 1, n)
    error = np.sqrt(((np.sum(f(x)**2) / n) - ((np.pi/2) / n)**2) / n)
    return error

def monte_carlo(N, f):
    a = 0
    b = 1
    xrand = np.random.uniform(a, b, N)
    my_sum = np.sum(f(xrand))
    area = (b - a) * my_sum / N
    error_val = error(my_sum, N)
    return area, error_val

def main():
    # b) Plotting the function
    x = np.linspace(0, 1, 1000)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("f(x) = sqrt(1 - x^2)")
    ax.set_xlabel("x values")
    ax.set_ylabel("f(x)")


    # Define sample sizes
    sample_sizes = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7]
    errors = []
    for N in sample_sizes:
        area, error_val = monte_carlo(N, f)
        print(f"For N = {N}, estimated area = {area}, error = {error_val}")
        errors.append(error_val)

    # e) Plot distribution of areas (histogram)
    fig, axe = plt.subplots()
    axe.hist(areas, bins=50, ec='black')
    axe.set_title('Distribution of Areas')
    axe.set_xlabel('Area')
    axe.set_ylabel('Frequency')
    plt.show()

main()


