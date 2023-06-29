#inserción y actualización:
person = {
  'name': 'juan',
  'last_name': 'garcia',
  'langs': ['python', 'javascript'],
  'age': 33
}

#update attribute:
print(person)

person['name'] = 'olme'
print(person)

#ajustes sobre el valor actual
person['age'] -= 1
print(person)

person['langs'].append('rust')
print(person)

#eliminar llave con del
del person['last_name']
print(person)

#eliminar atributo con pop, si no recibe argumento lanza error: TypeError: pop expected ...
person.pop('age')
print(person)

#obtener items del diccionario
print(person.items()) #return tuplas
#obtener keys:
print(person.keys()) #return list keys
#obtener values:
print(person.values()) #return list values