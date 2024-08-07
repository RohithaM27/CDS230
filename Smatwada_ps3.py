import math


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:13:13 2024

@author: Rohitha_matwada
"""


"""
Problem 1 - Exercise 3.1: A one-parameter function
"""
print("3.1") 
def one_para_func(x):
    y = (1 * math.exp(-x**2 / 2)) / math.sqrt(2 * math.pi)
    return y
    
for x in range(-5,6):
    y = one_para_func(x)
    print("({}, {:.6f})".format(x,y))
print()
"""
Problem 2 - Exercise 3.2: A two-parameter function
"""
print("3.2")# not printing the irght valeus, and explain it
def two_para_func(x,y):
    r = math.sqrt( (x**2) + (y**2) )
    return r
    
for i in range(0,11):
    x = i
    y = i    
    r = two_para_func(x, y)
    print("({},{}) : {:.2f}".format(x,y,r))
    
print()
"""
Problem 3 - Exercise 3.3: Getting a name’s initials
"""
print("3.3") 
name = input("Enter you name:")
print(name.lower())


def generate_initials(name):
    sep_name = name.split()
    initials = " "

    for i in sep_name:
        initials += i[0].upper()
    return initials
print("Initials: ", generate_initials(name))

print()
"""
Problem 4 - Exercise 3.4: Function that returns a dictionary (10 points)
"""
print("3.4") 

def count_elements(sequence):
    seq_dict = {}
    for z in sequence:
        if z in seq_dict:
            seq_dict[z] += 1
        else:
            seq_dict[z] = 1
    print(seq_dict)
print("Printing dictionaries for test cases")
state = "Mississippi"
temp_values = [72, 70, 75, 70, 72, 72, 71]

count_elements(state)
count_elements(temp_values)
    
print()
"""
Problem 5 - Exercise 3.5: Return multiple values from a function(10 points)
"""
print("3.5") 
def basic_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)  
    average = sum(numbers) / len(numbers)
    print(f"Minimum: {minimum} |", f"Maximum: {maximum} |", f"Average: {average}")

    
#list_numbers = input("Enter numbers separated by spaces: ")
#numbers = [float(x) for x in list_numbers.split()]
print("list_1_results:")
list_1_results = basic_stats([2, -1, 10, 5])
print("list_2_results:")
list_2_results = basic_stats([-11, -7, -5, -3, -2, 2, 3, 5, 7, 1])
print("list_3_results:")
list_3_results = basic_stats([4])
print("list_4_results:")
List_4_results = basic_stats([1, 1, 2, 3, 5, 8, 13])

print()

"""
Problem 6 - Exercise 3.6: Computing sum of n terms (10 points)
"""
print("3.6") 
def calculate_sum(n, p):
    total = 0
    for i in range(1, n+1):
        total += 1 / (i**p)
    return total

# Testing the function with n = 200 and p = 0.5,1,2,3,4
n = 200
p_values = [0.5, 1, 2, 3, 4]
for p in p_values:
    result = calculate_sum(n, p)
    print(f"The sum for n=200 and p={p} is: {result:.5f}")

# Discuss whether the values of the sums make sense
print("Yes, the values of this sum makes sense, because the function above calculates the sum of the given expression (1/i^p) starting from i=1 to i=200 using p in the list of values as the power of i. As p increases, the sum decreases, and larger the n gets, the sum calculates to a specific value based on thevalue of p. This behavior follows the properties of the given series")


    

