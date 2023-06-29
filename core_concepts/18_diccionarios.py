# diccionarios en python
my_dict = {}
print(my_dict)

my_dict = {
  'name': 'olga',
  'last_name': 'echeverry',
  'age': '34'
}

print(my_dict)

#cuantos elementos tiene el dict?
print(len(my_dict))

#leer el dict:
print(my_dict['name'])
print(my_dict['age'])

#con get si no existe el valor, lo maneja = None, sino lanza un error: KeyError
print(my_dict.get('last_name')) 
print(my_dict.get('e')) 

print('avion' in my_dict)
print('age' in my_dict)

#change properties
my_dict['name'] = 'olga maria'
print(my_dict)
