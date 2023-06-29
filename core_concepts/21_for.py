"""
for element in range(20):
  print(element)

print()
for element in range(15,20):
  print(element)
"""
#recorriendo estructuras:
my_list = [ 23, 34, 53, 29, 80]

for i in my_list:
  print(i)

#iterando tupla
my_tuple = ('sara', 'nena', 'victoria')
for name in my_tuple:
  print(name)

#dictionaries:
product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

for elem in product:
  print(elem) #solo llaves

for key in product:
  print(product[key]) #solo valores

for key, value in product.items():
  print('key:', key , ' value: ', value)

#lista de diccionarios: (response of bbdd)
people = [
  {
    'name': 'juan',
    'age': 34
  },
  {
    'name': 'sara',
    'age': 28
  },
  {
    'name': 'mary',
    'age': 29
  }
]

for person in people:
  print('name: ',person['name'])

