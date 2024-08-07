"""
Name: Rohitha
"""
import random

"""
Problem 1
"""
print("\n",40*"-","\n","Problem 1:\n",40*"-")

list_num = []

for i in range(1000):
    list_num.append(random.randint(-10,10))    
    
def my_avg(list_num):
    sum_of_list = sum(list_num)   
    count_of_list = len(list_num)
    average = sum(list_num)/len(list_num)
    return average
average_of_list = my_avg(list_num)
print("Average of random numbers in list_num", average_of_list)

"""
Problem 2
"""
print("\n",40*"-","\n","Problem 2:\n",40*"-")

def find_sequence(text, sequence):
    text = text.lower()
    locations = []
    
    start = 0
    while start >= 0:
        start = text.find(sequence.lower(), start)
        if start >= 0:
            locations.append(start)
            start += 1
            
    return locations


file = open('anna_karenina.txt', 'r').read()
seq1 = 'you know'
seq2 = 'Anna was'

location1 = find_sequence(file, seq1) 
location2 = find_sequence(file, seq2)

print("location1_of_seq1",len(location1)) 
print("location1_of_seq2",len(location2))

    


"""
Problem 3
"""
print("\n",40*"-","\n","Problem 3:\n",40*"-")
#a) Open and read the contents of the file into a list
with open("anna_karenina.txt", "r") as file:
    lines = file.readlines()

# b) Count total lines
total_lines = len(lines)
print("Total lines in the file:", total_lines)

#c) Count non-empty lines
non_empty_count = 0
for line in lines:
    if line != '\n':
        non_empty_count += 1
print("Total number of non empty lines in file:", non_empty_count)

# d) Count occurrences of the word "Stepan"
stepan_count = 0
for line in lines:
    stepan_count += line.count('Stepan')    
print("Number of occurrences of the word 'Stepan':", stepan_count)



"""
Problem 4
"""
print("\n",40*"-","\n","Problem 4:\n",40*"-")
# Read the file and store its contents into a string
def read_dna_sequence(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data
data = read_dna_sequence("dna.txt")

#a) Use len() to compute the length of the string, store the value in variable data len.
data_len = len(data)
print("length of the data string", data_len)
#b) count the number of occurrences of each a, c, g, t
a = data.count('a')
print("Total number of a's:", a)
c = data.count('c')
print("Total number of c's:", c)
g = data.count('g')
print("Total number of g's:", g)
t = data.count('t')
print("Total number of t's:", t)
#c)
sum_of_acgt = a+c+g+t
diff_sum_len = data_len - sum_of_acgt
print("difference:", diff_sum_len)
#d)
set_unique_data = set(data)
#e)
errors = set_unique_data - {'a', 'c', 'g', 't'}
print("erros:", errors)
# f) Count occurrences of each letter - unique and nucleotide
counts = {}
for letter in set_unique_data:
    counts[letter] = data.count(letter)

print("Occurrences of each letter:")
for letter in counts:
    print(letter, ":", counts[letter])




