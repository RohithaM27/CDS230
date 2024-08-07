import random
import math

"""
Name: Rohitha Matwada
"""

"""
Problem 1 - Exercise 2.1: Loops (20 points)

"""

# a) print the first 10 even numbers (1 pt)
print("(#a)printing the first 10 even numbers:")
for even in range(0,21):
    if even%2 == 0:
        print(even, end=" ")
print()
print("(#b)printing the first 10 odd numbers in reverse:")
#b) print the first 10 odd numbers in reverse (1 pt)
for odd in range(19,0,-2 ):
    print(odd)
print("(#c) print the first 10 non-zero multiples of 17")
#c) print the first 10 non-zero multiples of 17 (5 pts)
count = 0
for x in range(1,200):
    if x%17 == 0 and x !=0: 
        print(x, end=" ")
        count += 1
    if count ==  10:
        break
print()  
print("(#d) printing the sum of the digits of a number")
#d) display the sum of the digits of a number. Test with 7, 119, and 999 (5 pts)
sum_of_dig = 0
print("enter a number:")
num = int(input())

for digit in str(num):
    sum_of_dig += int(digit)

print("sum of digits:", sum_of_dig, end = " " )
print()

print("(#e) printing the product of the digits of a number")
#e) display the product of the digits of a number. Test with 7, 119, and 999 (5 pts)
prod_of_dig = 1
num = int(input("enter a number:"))

for digit in str(num):
    prod_of_dig *= int(digit)
print("product of digits:", prod_of_dig, end = " " )

print()
print("(#f) printing t all the numbers between 500 and 1000 (inclusive) that are divisible by 13 and by 2")
#f) display all the numbers between 500 and 1000 (inclusive) that are divisible by 13 and by 2 (3 pts)

for number in range(500, 1001):
    if number%13 == 0 and number%2 == 0:
        print(number, end=" ")
print()
"""
Problem 2 - Exercise 2.2: Random numbers (12 points)
"""
print("(2.2a) printing 100000 random inegers between -5 and 5")
#Use the above code to generate 100 000 random integers ranging from -5 to 5 and store them in a list called rand list
rand_list = []

for z in range(100000):
    rand_list.append(random.randint(-5, 5))

print()

print("(2.2b) printing the first 10 numbers from the list above")
#print the first 10 numbers

print(rand_list[0:10])

print("(2.2c) converting and printing the number of elements in rand_tuple ")
#convert the list to a tuple. print the number of elements in rand_tuple
rand_tuple = tuple(rand_list)
print(" number of elemetns in tuple are:", len(rand_tuple))

print()

print("(2.2d)Use a for loop to count and print the number of odd numbers in the tuple.")
#Use a for loop to count and print the number of odd numbers in the tuple

counter = 0
for odd_num in rand_tuple:
    if odd_num%2 != 0:
        counter += 1
print("number of odds in tuple:", counter)

print()

print("(2.2e) printing number of odd numbers in tuple if 0 was considered to be even ")
#How many odd numbers would you expect (Note that zero is considered to be an even number!)?
counter_odd = 0
for odd_num in rand_tuple:
    if odd_num%2 != 0 and odd_num != 0:
        counter_odd += 1
print("number of odds in tuple if 0 was considered to be even:", counter_odd)

print()


"""
Problem 3 - Exercise 2.3: Perfect numbers
"""
print("printing all the perfect numbers between 1 and 10000")
# A perfect number is a positive integer, greater than 1, that is equal to the sum of its divisors (excluding itself)

for perf_num in range(2,10000):
    sum_of_divisors = 0
    for i in range(1,perf_num):
        if perf_num%i == 0:
            sum_of_divisors += i
    if sum_of_divisors == perf_num:
        print(perf_num, end=" ")
            
print()       

"""
Problem 4 - Exercise 2.4: Projectile trajectory (12 points)
"""
# a)Defining variables
g = -9.81 # acceleartion due to gravity in ms^-2
u = 25 # initial speed in m/s
y = 0 # initial height in m
theta = math.radians(30) # projectile launch angle converted to radians

#(b)Evaluating and computing f(x) for the required x values
proj_values = []
for x in range(0, 11):
    f_x = (x*math.tan(theta))+(g*(x**2))/(2*(u**2)*(math.cos(theta))**2)+y
    proj_values.append(f_x)
    
proj_values_tuple = tuple(proj_values)
#print("f(x) values:", proj_values_tuple, end=" ")

print()

#printing table of x and f(x) values in the tuple

print("x    |    f(x)")
print("-" * 15)
for x in range(0,11):
    print("{:.0f}    |    {:.3f}".format(x, proj_values_tuple[x]))








