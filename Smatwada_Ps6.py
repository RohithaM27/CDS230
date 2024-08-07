"""
Name: Rohitha
"""
import numpy as np  # standard import
import matplotlib.pyplot as plt   # plotting package
np.set_printoptions(precision=3)
import math


"""
Problem 1
"""
print("\n",40*"-","\n","Problem 6.1:\n",40*"-")

a = -1
b = -4

x = np.linspace(-10, 10, 21)
y = a*x + b

fig, ax = plt.subplots()
ax.plot(x,y, label = 'y = ax + b', color = 'b')
ax.set_ylabel('y values')
ax.set_xlabel('x values')
ax.set_title('x vs y plot - y = ax + b')
ax.legend()
ax.grid()
"""
Problem 2
"""
print("\n",40*"-","\n","Problem 6.2:\n",40*"-")

x = np.linspace(-2*math.pi, 2*math.pi, 1000)
y = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x,y, label = 'y = cos(x)', color = 'g')
ax.set_ylabel('y values')
ax.set_xlabel('x values')
ax.set_title('x vs y plot - y = cos(x)')
ax.legend()
ax.grid()

"""
Problem 3
"""
print("\n",40*"-","\n","Problem 6.3:\n",40*"-")

real= np.array([250.86244899999997,
 339.27466000000004,
 105.66256599999997,
 285.836143,
 103.10954700000002,
 612.339172,
 980.645671,
 94.928631,
 106.02109500000006,
 395.5160169999999,
 234.74280199999998,
 453.741622,
 877.775261,
 735.760669,
 61.10505899999998,
 141.61726999999996,
 232.5462869999999,
 485.12524600000006,
 179.09305399999994,
 763.1764880000001,
 714.7048809999999])
predicted1= np.array([182.60651299999995,
 307.566548,
 90.35535699999991,
 201.7277200000001,
 18.93160899999998,
 586.741282,
 1073.734861,
 121.74960699999997,
 93.16468200000008,
 345.728877,
 181.38813499999992,
 448.568219,
 969.430382,
 814.0775389999999,
 49.854831000000104,
 82.98331800000005,
 180.20239199999992,
 498.6508180000001,
 269.52380199999993,
 692.147555,
 631.618131])
predicted2= np.array([133.55121299999996,
 513.7071780000001,
 -73.27098520000004,
 209.725911,
 162.99760199999992,
 662.4478320000001,
 1037.447472,
 4.68638999999996,
 65.0330879999999,
 505.19044800000006,
 11.728526999999985,
 404.182947,
 791.4509310000001,
 890.973888,
258.784257,
 46.07318499999997,
 447.6741669999999,
 283.4361799999999,
 346.06016999999997,
 855.629737,
 896.855581])
predicted3= np.array([289.2418520000001,
 299.48912700000005,
 111.46630400000004,
 291.5770600000001,
 89.33233300000006,
 618.674814,
 970.1700599999999,
 112.60857499999997,
 98.59951999999998,
 398.40663100000006,
 242.85708599999998,
 440.71055,
 904.3781570000001,
 726.489816,
 74.0629080000001,
 154.11110000000008,
 205.761704,
 477.7552599999999,
 205.525527,
 799.8071649999999,
 700.0304719999999])
predicted4= np.array([239.10130800000002,
 368.3231209999999,
 153.67522400000007,
 360.1781490000001,
 100.85696699999994,
 665.134624,
 981.703675,
 24.189307999999983,
 115.63781799999992,
 450.8444300000001,
 274.82238699999994,
 413.2511219999999,
 895.693964,
 781.094654,
 55.89924399999995,
124.72796799999992,
 204.49151299999994,
 546.7008149999999,
 179.66186399999992,
 821.1714079999999,
 653.113871])
predicted5= np.array([409.62601500000005,
 453.25078099999996,
 128.6927659999999,
 253.23214499999995,
 11.672974999999951,
 617.889011,
 1116.745579,
 76.21661900000004,
 241.6212660000001,
 426.0338609999999,
 161.6892029999999,
 405.61425800000006,
 970.8265960000001,
 738.837106,
 214.05676799999992,
 277.983739,
 347.5145889999999,
 490.12546199999997,
 60.997380999999905,
 735.633865,
 689.3939889999999])

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(real, label='Real', color='black', linewidth=3)


ax.plot(predicted1, label='Model 1', color = 'orange')
ax.plot(predicted2, label='Model 2', color = 'green')
ax.plot(predicted3, label='Model 3', color = 'yellow')
ax.plot(predicted4, label='Model 4', color = 'blue')
ax.plot(predicted5, label='Model 5', color = 'purple')

ax.set_xlabel("X values")
ax.set_ylabel("Y values")
ax.set_title("real plot vs predicted model plots")
ax.legend()

def performance(real, predicted):
    performance_result = np.mean(np.abs(real - predicted))
    return performance_result
    
performance_model1 = performance(real, predicted1)
performance_model2 = performance(real, predicted2)
performance_model3 = performance(real, predicted3)
performance_model4 = performance(real, predicted4)
performance_model5 = performance(real, predicted5)    

print("Performance result of Model 1:", performance_model1)
print("Performance result of Model 2:", performance_model2)
print("Performance result of Model 3:", performance_model3)
print("Performance result of Model 4:", performance_model4)
print("Performance result of Model 5:", performance_model5)






"""
Problem 4
"""
print("\n",40*"-","\n","Problem 6.4:\n",40*"-")

class Product:
    
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        
    def info(self):
        print(f'Product information. Name: {self.name}, description: {self.description}, price: ${self.price}')
        
iphone1 = Product("iphone1", "This is an old phone model", "599.0")
iphone2 = Product("iphone2", "This is a new phone model", "799.0")

iphone1.info()
print()
iphone2.info()


"""
Problem 5
"""
print("\n",40*"-","\n","Problem 6.5:\n",40*"-")

class Vehicle:
    def __init__(self, make, model, fuel='gas'):
        self.make = make
        self.model = model
        self.fuel = fuel
        
    
class Car(Vehicle):
    number_of_wheels = 4
    
    def __init__(self, make, model, fuel='gas'):
        super().__init__(make, model, fuel)
    
class Truck(Vehicle):
    number_of_wheels = 6
    
    def __init__(self, make, model, fuel='disel'):
        super().__init__(make, model, fuel)

car_ins = Car("Toyota", "Prius")
truck_ins = Truck("Ford", "F350")

print("Toyota Priyua fuel type : ", car_ins.fuel)
print("Ford F350 fuel type : ", truck_ins.fuel)


    
