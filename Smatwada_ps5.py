"""
Name: Rohitha
"""
import numpy as np
np.set_printoptions(precision=3)
# This guarantees the code will generate the same set of random numbers whenever executed:
np.random.seed(123)

"""
Problem 1
"""
print("\n",40*"-","\n","Problem 1 - Exercise5.1 :\n",40*"-")

null_vector = np.zeros(11)
print(null_vector)

"""
Problem 2
"""
print("\n",40*"-","\n","Problem 2 - Exercise5.2 :\n",40*"-")

matrix_3_5 = np.ones((3,5))
print(matrix_3_5)

"""
Problem 3
"""
print("\n",40*"-","\n","Problem 3 - Exercise5.3 :\n",40*"-")

linear_vector = np.linspace(0.0, 10.0, 10)
print(linear_vector)


"""
Problem 4
"""
print("\n",40*"-","\n","Problem 4 - Exercise5.4 :\n",40*"-")

matrix_4_3 = np.arange(1,13).reshape((4,3))

print(matrix_4_3)

"""
Problem 5
"""
print("\n",40*"-","\n","Problem 5 - Exercise5.5 :\n",40*"-")

vector = np.arange(20,31)
#print(vector)
a = vector[::-1]
print(a)

"""
Problem 6
"""
print("\n",40*"-","\n","Problem 6 - Exercise5.6 :\n",40*"-")

total_int = 15 - (- 5) + 1
linearly_spaced = np.linspace(-5, 15, total_int)
print(linearly_spaced)

"""
Problem 7
"""
print("\n",40*"-","\n","Problem 7 - Exercise5.7 :\n",40*"-")

array_1D = np.arange(-10.0, 10.0, 0.1)
print("size of 1D array : ", array_1D.size)

"""
Problem 8
"""
print("\n",40*"-","\n","Problem 8 - Exercise5.8 :\n",40*"-")

array2_1D = np.ones(100)

array2_1D[::2] = -1

print("first 10 numbers :", array2_1D[0:10])

"""
Problem 9
"""
print("\n",40*"-","\n","Problem 9 - Exercise5.9 :\n",40*"-")

B = np.array([[1, 2, -3], [3, 4, -1]])
print("B", B)
print()
A = np.array([[2, 5, -1], [1, 4, 5], [2, 1, -6]])
print("A", A)
print()
y = np.array([-1,3, 7])
print("y", y)
print()
z = np.array([[13],[0],[2]])
print("z", z)
"""
Problem 10
"""
print("\n",40*"-","\n","Problem 10 - Exercise5.10 :\n",40*"-")
# array with celcius temperature
C = np.arange(-40,100)
# converts celcius to farenheit in the array
F = (( 9 / 5 ) * C) + 32

print(f"first {F[0]} and last {F[-1]} temperatures" )

"""
Problem 11
"""
print("\n",40*"-","\n","Problem 11 - Exercise5.11 :\n",40*"-")

rand_array = np.random.randint(-10,11, size = (4,6))

locations = [(1, 1), (2, 3), (3, 0), (0, 5)]
for pos in locations:
    value = rand_array[pos]
    print(f"Value at location {pos}: {value}")

"""
Problem 12
"""
print("\n",40*"-","\n","Problem 12 - Exercise5.12 :\n",40*"-")

#a Generate 10^6 normally distributed random numbers
my_vec = np.random.normal(loc = 0, scale = 1, size = 10**6 )
#b Calculate avg of my_vector using for loop
total = 0
for i in my_vec:
    total += i
average = total/len(my_vec)
print("The average of numbers in my_vec :", average )   
#c Compute the average using the numpy mean() function
print()
average_numpy = np.mean(my_vec)
print("The average of numbers in my_vec using numpy function :", average )   
#d Does the average value of the random numbers make sense to you?
"""
The first method used to calculate the average is a basic mathematical way 
to compute average of numbers. The secong method is a numpy function to get
the average. The average value of the random numbers makes sense 
because the mean of a large number of normally distributed random numbers
has a mean of 0. It also has to do with the symmetry of normal distribution

"""



"""
Problem 13
"""
print("\n",40*"-","\n","Problem 13 - Exercise5.13 :\n",40*"-")
a = np.random.randint(1,11, size =10)
b = np.random.randint(1,11, size =10)
c = np.random.randint(1,11, size =10)
d_array = a*b + c

print("d_array :", d_array)

"""
Problem 14
"""
print("\n",40*"-","\n","Problem 14 - Exercise5.14 :\n",40*"-")

def position(t):
    g = -9.81 # in m/s^2
    distance = 0.5*g*(t**2)
    return distance
"""
a function called position that takes in an array t containing time 
measurements and returns a distance array where d is in meters and 
g is a constant with value −9.81 m/s2.
d = 0.5 * g * ( t ** 2 )
"""
time_array = np.arange(0,10.1,0.1)

d_at_1_sec = position(1)
print("Distance at t = 1 :", d_at_1_sec)

#check if the results match the expected 
expected_result = 0.5 * (-9.81) * ( 1 ** 2)
if np.isclose(d_at_1_sec, expected_result):
    print("The computed result at one second matches the expected results")
    print("Expected results: ", expected_result)
else:
    print("The computed result at one second doesn' match the expected results")



        



