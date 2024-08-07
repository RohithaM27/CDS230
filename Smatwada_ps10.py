#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:26:40 2024

@author: rohitha_matwada
"""

import numpy as np
import matplotlib.pyplot as plt
import random

"""
Problem 2
"""
print("\n",40*"-","\n","Problem 10.2:\n",40*"-")

# 1) Let the values for the mean and the spread of the distribution be 10.0 and 2.0 respectively, then produce 1000 pseudo-random numbers with this command:

u = 10.0
s = 2.0
total_number_of_data_points = 1000

# Generate Gaussian-distributed random numbers
randomgauss = np.random.normal(loc=u, scale=s, size=total_number_of_data_points)

# 2) Plot a histogram of your array ”randomgauss”, using the function ”plt.hist”. 
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(randomgauss, bins=50, color='red')
ax.set_title('Histogram of Gaussian Distribution: 1000 pseudo-random numbers ', fontsize=15)
ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Frequency', fontsize=15)

print("Mean of randomgauss (1000):", np.mean(randomgauss))
print("Standard deviation of randomgauss (1000):", np.std(randomgauss))

#4) Repeat steps 1-3 with 1 million total number of data points
total_number_of_data_points = 1000000
randomgauss = np.random.normal(loc=u, scale=s, size=total_number_of_data_points)

# Plot histogram with 50 bins
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(randomgauss, bins=50, color='green')
plt.title('Histogram of Gaussian Distribution: 1000000 pseudo-random numbers ', fontsize=15)
plt.xlabel('Value', fontsize=15)
plt.ylabel('Frequency', fontsize=15)

print("Mean of randomgauss (1000000):", np.mean(randomgauss))
print("Standard deviation of randomgauss (1000000):", np.std(randomgauss))

"""
Does the histogram resemble a normal distribution? Invoke the Law of
Large Numbers to explain your histograms???
Ans : The histogram resembles a normal distribution more closely as 
the number of data points increases due to the Law of Large Numbers.
As the data points increased from 1000 to 1 million, the sample size
increases and now the histogram looks more symmetrically bell shaped.

The Law of Large Numbers states that as the sample size increases, the 
sample mean becomes closer to the true population mean, and the sample
standard deviation becomes closer to the true population standard deviation. 
This concept results in the histpogram of gaussian distribution to resemble
a normal distribution.
"""

"""
Problem 3
"""
print("\n",40*"-","\n","Problem 10.3:\n",40*"-")

# Define the number of balls in each color
red_balls = 10
blue_balls = 10
yellow_balls = 10
purple_balls = 10
total_balls = 40 #number of total outcomes

# Define the number of trials
num_trials = 100000

# Initialize the counter for the desired outcome
num_desired_outcome = 0

for _ in range(num_trials):
    # Draw 10 balls at random from the hat
    balls_drawn = random.sample(range(total_balls), 10)
    
    red_count = 0
    yellow_count = 0
    for ball in balls_drawn:
        if ball < red_balls:
            red_count += 1
        elif ball < red_balls + yellow_balls:
            yellow_count += 1

# Check if the sample contains two red and two yellow balls
    if red_count == 2 and yellow_count == 2:
        num_desired_outcome += 1

# Calculate the estimated probability
probability = num_desired_outcome / num_trials
print("Estimated probability:", probability)

"""
Problem 4 
"""
print("\n",40*"-","\n","Problem 10.4:\n",40*"-")

#a) Write code to compute the signal η. Define the constants and time array as specified above.

# Define variables
A = 1
T = 2 * np.pi

# Time Array
i = np.linspace(0,200,201)
ti = (T/40)*i

# originial signal
n = A*np.sin( ( ( 2 * np.pi ) / T ) * ti) 

# b)Add noise to the signal, that is, create a new array ηnoisy. create subplots

Ei = np.random.normal(loc = 0, scale = 0.1 , size = 201 )

# noisy equation
n_noisy = n + Ei


fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Plotting noise in the first subplot
ax[0].plot(ti, Ei, 'red' , label='Noise / Ei')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Frequency')
ax[0].set_title('Noise plot')
ax[0].legend()

# Plotting original signal and noisy signal in the second subplot
ax[1].plot(ti, n,'blue', label='original signal')
ax[1].plot(ti, n_noisy,'green', label='noisy signal')
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Frequency')
ax[1].set_title('Original signal and Nnoisy signal plot')
ax[1].legend()

# c) remove the noise 

def filter_noise(signal):
       sig = signal[:]
       i = np.arange(1, len(sig) - 1)
       sig[1 : len(sig) - 1] = 1/4 * (sig[i - 1] + 2*sig[i] + sig[i + 1])
       return sig
   
n_clean = filter_noise(n_noisy)


fig, axe = plt.subplots(1, 2, figsize=(12, 6))

# Plotting noise in the first subplot
axe[0].plot(ti, n, 'red' , label='original signal')
axe[0].plot(ti, n_clean, 'green' , label='filtered signal')
axe[0].set_xlabel('Time')
axe[0].set_ylabel('Frequency')
axe[0].set_title('Original Signal and Filtered Signal')
axe[0].legend()

# Plotting original signal and noisy signal in the second subplot
axe[1].plot(ti, n_clean - n,'blue', label='filtered signal - original signal')
axe[1].set_xlabel('Time')
axe[1].set_ylabel('Frequency')
axe[1].set_title('Difference between Filtered and Original Signal')
axe[1].legend()

"""
Did the filter noise function remove most of the noise????

Ans: The overal structure and features of the orginal signal stays the same,
but the frequency changes in the plot after filtering the noise. The filter 
noise function reduces high freqency in the noise filtered plot.
The " filtered signal - original signal plot" shows the filtered noise signal.
"""