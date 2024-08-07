import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)

"""
Name: Rohitha
"""

"""
Problem 1
"""
print("\n",40*"-","\n","Problem 7.1:\n",40*"-")

"""
a) The common difference is what you get by subtracting
two consequtive terms like, subtractice frist term from 
second term. The common difference stays the same througout
the sequence of numbers.

Here the common difference difference is 11 according to the
sequence of numbers given.

second term - first term = 14 - 3 = 11
"""
s0 = 3
com_diff = 11

def linear_model(s0, com_diff, n):
   return s0 + (n-1)*com_diff  

gen15th = linear_model(s0, com_diff, 15)
print("Number of members in the 15th gen:", gen15th)
gen31st = linear_model(s0, com_diff, 31)
print("Number of members in the 31st gen:", gen31st)


"""
Problem 2
"""
print("\n",40*"-","\n","Problem 7.2:\n",40*"-")

"""
a) The common ratio is what you get by dividing the second 
   term by the first one in a sequence. 
   second term / first term = 9.42/3 = 3.14
   
   common ratio here is 3.14
"""
s0 = 3
com_ratio = 3.14
def geometric_growth_model(s0, com_ratio, n):
    return 3*(com_ratio**(n-1))
p9 = geometric_growth_model(s0, com_ratio, 9)
print("The population growth of bacteria in 9th gen:", p9)
p20 = geometric_growth_model(s0, com_ratio, 20)
print("The population growth of bacteria in 20th gen:", p20)


"""
Problem 3
"""
print("\n",40*"-","\n","Problem 7.3:\n",40*"-")

altitude = np.array([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000,
4500, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])

air_density = np.array([1.225, 1.167, 1.112, 1.058, 1.006, 0.957, 0.909, 0.863,
0.819, 0.777, 0.736, 0.660, 0.590, 0.526, 0.467, 0.413, 0.365, 0.312,
0.226, 0.228, 0.195])

fig, ax = plt.subplots()
ax.set_xlabel("Altitude(m)")
ax.set_ylabel(" Air Density(kg/m3) ")
ax.set_title(" Air Density vs Altitude ")
ax.plot( altitude ,air_density, label = "y = mx + b", color = 'black')
ax.legend()
ax.grid()

slope = ( air_density[-1] - air_density[0] )/ (altitude[-1] - altitude[0])
b = air_density[0] - slope*(altitude[0])

"""
The linear mmodel function takes in the altitude value (x value) and returns
the y value which is air density. The function calculates y by using the formula
y = mx + b.
"""
def linear_model(x):
    y = slope * x + b
    return y

alt_2250 = 2250
alt_20000 = 20000
print(f'Density at 2250 m altitude is {linear_model(alt_2250):.4f} kg/m3')
print(f'Density at 20000 m altitude is {linear_model(alt_20000):.4f} kg/m3')

"""
Problem 4
"""
print("\n",40*"-","\n","Problem 7.4:\n",40*"-")

subplt1 = """1951,2569951208
1952,2616316758
1953,2662543504
1954,2709178365
1955,2756662517
1956,2805328910
1957,2855404933
1958,2907023467
1959,2960240049
1960,3015085838
1961,3071623124
1962,3129995156
1963,3190446183
1964,3253262811
1965,3318598296
1966,3386535759
1967,3456874782
1968,3529117645
1969,3602582433
1970,3676727865
1971,3751454788
1972,3826757615
1973,3902316828
1974,3977783768
1975,4052954392
1976,4127653812
1977,4202040817
1978,4276676636
1979,4352350393
1980,4429660149
1981,4508601232
1982,4589057229
1983,4671352595
1984,4755854655
1985,4842705541
1986,4932112905
1987,5023677382
1988,5116168638
1989,5207930480
1990,5297738844
1991,5385171977
1992,5470448447
1993,5553789455
1994,5635670131
1995,5716485992
1996,5796242146
1997,5874914801
1998,5952873494
1999,6030583814
2000,6108424718
2001,6186543057
2002,6265005402
2003,6344003287
2004,6423719971
2005,6504280993
2006,6585760192
2007,6668138074
2008,6751310827
2009,6835108522
2010,6919368228
2011,7004042402
2012,7089048309
2013,7174135279
2014,7258995892
2015,7343380299
2016,7427157079
2017,7510270208
2018,7592641463
2019,7674218669
2020,7754954225
2021,7834779420
2022,7913638043
2023,7991520040"""

subplt2 = """2023,7991520040
2024,8068434258
2025,8144386957
2026,8219357727
2027,8293328034
2028,8366311838
2029,8438333140
2030,8509410159
2031,8579544930
2032,8648732275
2033,8716974154
2034,8784272290
2035,8850628027
2036,8916036314
2037,8980497153
2038,9044021863
2039,9106625508
2040,9168314810
2041,9229088813
2042,9288930502
2043,9347809640
2044,9405686128
2045,9462526252
2046,9518317740
2047,9573052055
2048,9626703497
2049,9679244145
2050,9730653103
2051,9780925140
2052,9830060747
2053,9878054043
2054,9924901332
2055,9970606232
2056,10015171511
2057,10058616334
2058,10100982292
2059,10142323204
2060,10182685100
2061,10222090083
2062,10260552761
2063,10298103856
2064,10334774690
2065,10370592051
2066,10405576570
2067,10439741399
2068,10473095060
2069,10505640797
2070,10537382981
2071,10568334032
2072,10598504167
2073,10627891474
2074,10656489672
2075,10684296986
2076,10711318933
2077,10737567885
2078,10763057186
2079,10787803360
2080,10811821143
2081,10835117371
2082,10857699972
2083,10879588360
2084,10900804094
2085,10921363657
2086,10941274809
2087,10960537164
2088,10979149734
2089,10997107811
2090,11014406137
2091,11031039978
2092,11047004654
2093,11062295173
2094,11076904361
2095,11090822611
2096,11104037489
2097,11116533330
2098,11128291145
2099,11139289195
2100,1114950201"""

def world_pop(data):
    years = []
    population = []
    lines = data.strip().split('\n')
    for line in lines:
        yr, pop = line.split(',')
        years.append(int(yr))
        population.append(int(pop))
    return years, population

plt1_years, plt1_population = world_pop(subplt1)
plt2_years, plt2_population = world_pop(subplt2)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize = (14,6))
#subplot1
ax[0].set_xlabel(" Year:1951-2023")
ax[0].set_ylabel(" Population ")
ax[0].set_title(" Total World Population")
ax[0].plot(plt1_years, plt1_population, color = 'blue')
ax[0].grid()
#subplot2
ax[1].set_xlabel(" Year:2023-2100 ")
ax[1].set_ylabel(" Population ")
ax[1].set_title(" Total World Population")
ax[1].plot(plt2_years, plt2_population, color = 'red')
ax[1].grid()

"""
The world population growth rate from 1951-2023 is close to linearly growing,
whereas the from 2023-2100, the grow rate is slowly and close to linearly 
growing and few years before 2100, the growth rate fastly dips. The growth rate
goes down by the time it reaches 2100.
"""

# Subplot 1: Growth rate calculation
initial_pop_subplt1 =  plt1_population[0]
final_pop_subplt1 =  plt1_population[-1]
number_of_years_subplt1 = 2023-1951

growth_rate_subplot1 = (final_pop_subplt1 - initial_pop_subplt1) / number_of_years_subplt1
print(f"Population growth rate for 1951-2023 is about {growth_rate_subplot1:.0f} people per year")

# Subplot 2: Growth rate calculation
initial_pop_subplt2 =  plt2_population[0]
final_popu_subplt2 =  plt2_population[-1]
number_of_years_subplt2 = 2100-2023
growth_rate_subplot2 = (final_popu_subplt2 - initial_pop_subplt2) / number_of_years_subplt2
print(f"Population growth rate for 2023-2100 is about {growth_rate_subplot2:.0f} people per year")


"""
Problem 5
"""
print("\n",40*"-","\n","Problem 5:\n",40*"-")

# Initial conditions
r = 0.35 # decay rate
initial_impurity = 405.0 # parts per gallon
N = 10   # choose a number of applications

impurities_y = [initial_impurity]
applications_x = [0]


for i in range(N):
    impurity= 0
    impurity = impurities_y[-1] * (1 - r)

    impurities_y.append(impurity)
    applications_x.append(i+1)
    if impurity < 0.6:
        break    
print(impurities_y , applications_x)

fig, ax = plt.subplots()
ax.plot(applications_x, impurities_y, label = 'exponential decal', color = 'red')
ax.set_ylabel("Impurities (parts/gal)")
ax.set_xlabel("Number of applications of solvent")
ax.set_title(" Impurities vs numbers of applications")
ax.grid()

print(f"It took {len(impurities_y) - 1} applications of the solvent for the water to be drinkable.")
    
    

