#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:46:53 2024

@author: rohitha_matwada
"""

import numpy as np
import matplotlib.pyplot as plt
import random

class LotkaVolterra():
    def __init__(self, params, dt, t_max, x0, y0):
        self.alpha = params[0]
        self.beta = params[1]
        self.gamma = params[2]
        self.delta = params[3]
        self.dt = dt
        self.N = int(t_max/dt)
        # Initial conditions
        self.t = np.arange(0, t_max, dt)
        self.x = np.zeros(self.N)
        self.y = np.zeros(self.N)
        self.x[0] = x0
        self.y[0] = y0

    def update(self, amp=0):
        # Perform simulation using the Lotka-Volterra equations
        for i in range(1, self.N):
            if amp:
                self.x[i] = self.x[i-1] + ( self.alpha*self.x[i-1] - self.beta*self.x[i-1]*self.y[i-1] )*self.dt + noise(amp)
            else:
                self.x[i] = self.x[i-1] + ( self.alpha*self.x[i-1] - self.beta*self.x[i-1]*self.y[i-1] )*self.dt
            self.y[i] = self.y[i-1] + (-self.gamma*self.y[i-1] + self.delta*self.x[i-1]*self.y[i-1])*self.dt

    def visualize(self):
        fig, ax = plt.subplots(1,2, figsize=(12,6))
        ax[0].plot(self.t, self.x, label='Prey')
        ax[0].plot(self.t, self.y, label='Predator')
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Population')
        ax[0].set_title('Predator-prey dynamics')
        ax[0].legend()
        ax[0].grid()
        ax[1].plot(self.x, self.y)
        ax[1].set_xlabel('Prey population')
        ax[1].set_ylabel('Predator population')
        ax[1].set_title('Phase space')
        # Mark the ICs
        ax[1].scatter(self.x[0], self.y[0], color='red')
        ax[1].grid()

        plt.tight_layout()
        plt.show()

def noise(amp):
    """ Add noise with some amplitude factor (amp) """
    return (amp * random.uniform(-1,1))
        
