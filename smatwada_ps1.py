import math

"""
Name: Rohitha Matwada
"""

"""
Problem 1 - Exercise 1.1
"""
prob_a = 4 + (5/4)
print("{:.2f}".format(prob_a))

prob_b = 19 + 48**-4
print("{:.2f}".format(prob_b))

prob_c = ((math.cos(math.pi))**2)-((math.sin(math.pi)**2))
print("{:.2f}".format(prob_c))

prob_d = (1)/(math.sqrt(2*math.pi))*math.e
print("{:.2f}".format(prob_d))

prob_e = -(4+(5**3)-(1/3))/((2**3)*18)
print("{:.2f}".format(prob_e))


"""
Problem 2- Exercise 1.2
"""

print('''
a) data4analysis - legal name, but readability can be improved if underscores were used in place of spaces. Not a good name.
b) 7mac11 - illegal, becuase a variable name can't start with a number
    corrected : mac_11
c) iHeartData! - illegal name, you can only use alphanumeric characters and underscores in variables. "!" can't be used.
    corrected : iHeartData
d) j - legal name, but not very meaning full so not a good name
e) data-set - illegal name, you can only use alphanumeric characters and underscores in variables. "-" can't be used.
    corrected : data_set
f) data set - illegal name, you can only use alphanumeric characters and underscores in variables. Spaces can't be used.
    corrected : data_set
g) len - illegal ,becuase "len" is a python keyword or method to print the length of a string(count of characters).
    Corrected : length
h) thisOldVariable - legal name, but words can be seperated by underscores. Ex: this_Old_Variable
i) variablesRgr8 - legal name, but words can be seperated by underscores. Ex: variables_Rgr8
j) this_is_a_variable_i_will_use_for_analysis_results - legal name, but not a good name, becuase it's too long.
''')


"""
Problem 3 - Exercise 1.3
"""
s = "Computers are incredibly fast, accurate, and stupid. Human beings are incredibly slow, inaccurate, and brilliant. Together they are powerful beyond imagination."

#a
print("length of s:", len(s))
#b
print("Number of commas in s:", s.count(","))
#c
var_index_H = s.index('H')
print("Index of H in s:" , var_index_H)
#d
print("printing Human using slicing method:", s[53:58])
#e
print("replacing i's in s with l's:", s.replace("i","l"))
print("printing s:", s)

print()
"""
Problem 4 - Exercise 1.4
"""
x = 3
y = 9
z = "2.4"
a = True

#a
print("a)", x/y)
#b
print("b)", x//y)
#c
print("c)", x%y)
#d
print("d) can't print y/x*z becuase can't multiply an integer by a string")
#e
print("e)",float(x)/float(z))
#f
print("f) int(x)/int(z) gives an error becuase z, the string, can't be converted to an interger directly since it has a decimal number. Z has to be converted to float first, and then to an integer" ) 
#g
print("g)", a+x) # what was this??
#h
print("h)", a+a)
#i)
print("i)", x/y < 0.3)
#j)
print("j)", str(3)>z)# what was this??





"""
Problem 5
"""
print()
#Defining Variables
G = 6.67*(10**-11) #Newton's gravitational constant in m^3 kg^-1 s^-2
M = 5.97*(10**24) #Mass of the Earth in kg
R = 6371 #Radius in km

#a)
T = 5400  #90*60/converted to seconds
Altitude = ((G*M*(T**2))/(4*(math.pi**2)))**(1/3) - R #Set up for calculating the altitude
print("Altitude in meters of satellites that orbit the Earth in 90 minutes:", Altitude )

T = 2700 # 45*60/converted to seconds 
Altitude = ((G*M*(T**2))/(4*(math.pi**2)))**(1/3) - R #Set up for calculating the altitude
print("Altitude in meters of satellites that orbit the Earth in 45 minutes:", Altitude )

T = 86148 # 23.93*60*60/converted to seconds - Geosynchronous
Altitude = ((G*M*(T**2))/(4*(math.pi**2)))**(1/3) - R #Set up for calculating the altitude
print("Altitude in meters of satellites that orbit the Earth once a day/ in 23.93 hours:", Altitude )


T = 86400 # 24*60*60/converted to seconds 
Altitude = ((G*M*(T**2))/(4*(math.pi**2)))**(1/3) - R #Set up for calculating the altitude
print("Altitude in meters of satellites that orbit the Earth in 24 hours:", Altitude )

#b)
print("The difference between the altitude for the satellites orbiting the Earth in 24 hours vs. in 23.93 hours =  42220539.17617497 - 42138391.329895645 = 82147.8462793231 seconds")










