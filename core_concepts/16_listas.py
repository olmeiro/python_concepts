#listas: con corchetes (arrays o vector)
#Permite guardar varios tipos de elementos
number = [1,2,3,4,5,6,7,8,9]
print(number)
print(type(number))

task = ['make a dishes', 'play video games']
print(task)

types = [1, True, 'hola']
print(types)

print(number[0])
print(task[0])

#mutacion: no se permite en strings
#text = 'hola'
#text[0] = 'w' #error

#una lista si es mutable:
task[0] = 'tidy up'
print(task)

task[0] = 'do the dishes'
print(task)

print(number[:3]) #partes de la list
print(True in types)
print('hola' in types)