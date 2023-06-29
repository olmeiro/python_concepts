set_countries = {'India', 'USA', 'China', 'Russia', 'India', 'USA'}

print(set_countries) #elimina los duplicados
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set_types = {1, 2.0, 'three', (4, 5, 6), True, None}

#conjuntos a partir de otros tipos de datos

#from string
set_from_string = set('hello')
print(set_from_string)

set_from_numbers = set(range(10))
print(set_from_numbers)

#from tuple
set_from_tuple = set(('abc', 'cvc', 'abc', 'xyz', 'rfc'))
print(set_from_tuple)

#from list
set_from_list = set(['abc', 'cvc', 'abc', 'xyz', 'rfc'])
print(set_from_list)

#sacar los elementos de un conjunto de números no repetidos
set_from_list_numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,3])
print(set_from_list_numbers)
result = list(set_from_list_numbers)
print(result)