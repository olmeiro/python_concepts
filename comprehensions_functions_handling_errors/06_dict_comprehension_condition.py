# dict comprehension with condition

import random
countries = ['india', 'usa', 'uk', 'china', 'japan']

population = {country:random.randint(1, 100) for country in countries}
print(population)

# we want to create a new dict with countries having population greater than 1 million

population_v1 = {country:population[country] for country in population if population[country] > 50}
print(population_v1)

#other way of doing the same thing
population_v2 = {country:pop for (country, pop) in population.items() if pop > 50} # items() returns a list of tuples
print(population_v2)

# other way of doing the same thing
population_v3 = {country:population for (country, population) in population.items() if population > 50}
print(population_v3)

# other example
text = 'hola soy una cadena de texto'
unique_vowels = {characters: characters.upper() for characters in text if characters in 'aeiou'}
print(unique_vowels)

# frecuency vowels
frequency_vowels = {characters: text.count(characters) for characters in text if characters in 'aeiou'}
print(frequency_vowels)

