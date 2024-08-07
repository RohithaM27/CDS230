#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 22:09:00 2024

@author: rohitha_matwada
"""

import numpy as np
'''
a = np.array([1,2,3,4,5])
print(a)
print(type(a))

a_mul = np.array([[[1, 2, 3, 2],
                  [4, 5, 6, 3],
                  [7, 8, 9, 5]],
                  
                  [[1, 2, 3, 2],
                   [4, 5, 6, 3],
                   [7, 8, 9, 5]] 
                  ]) 
print(a_mul[0])
print(a_mul[0, 1])

print(a_mul.shape) # (3 lists, 4 elements)/ (3 rows, 4 columns)

print (a_mul.ndim)

print (a_mul.size)
print(type(a_mul))
'''

'''
a = np.full((2,3,4), 9)
print(a)

b = np.zeros((10,5,2))
print(b)

c = np.ones((10,5,2))
print(c)

x_values = np.arange(0, 1000, 5) # (start, stop - not incluses, step)
print(x_values)

y_values = np.linspace(0, 1000, 2) # (start, stop - included if endpoint is true which is default, number of values - spreads out numbers evenly.])
'''
'''
l1 = [1,2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]

a1 = np.array(l1)
a2 = np.array(l2)

print

'''
X = [[12, 7],
     [4 ,5],
     [3 ,8]]

result = [[0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)
