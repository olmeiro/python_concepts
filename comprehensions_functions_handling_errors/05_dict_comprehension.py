# dict comprehension

#without dict comprehension
dict = {}
for i in range(1,11):
    dict[i] = i**2

print(dict)

#with dict comprehension
dict_v1 = {i:i**2 for i in range(1,11)}
print(dict_v1)

# dict from list with comprehension
import random
countries = ['india', 'usa', 'uk', 'china', 'japan']
population = {}
for country in countries:
    population[country] = random.randint(100000, 10000000)

print(population)

# using dict comprehension
population_v1 = {country:random.randint(100000, 10000000) for country in countries}

print(population_v1)

# one more example: from 2 list we want to create a dict
names = ['john', 'jane', 'joe', 'jack']
ages = [20, 30, 40, 50]

# without dict comprehension
dict_v2 = {}
for i in range(len(names)):
    dict_v2[names[i]] = ages[i]

print(dict_v2)

# with dict comprehension
dict_v3 = {names[i]:ages[i] for i in range(len(names))}
print(dict_v3)

# other form using zip: zip is a function which takes 2 or more list and returns a list of tuples
dict_v4 = {name:age for (name, age) in zip(names, ages)}
print(dict_v4)