numbers = (1, 2, 3, 4, 5)
strings = ('nico', 'juan', 'sara', 'sara')
print(numbers)
print(type(numbers))
print(strings)
print(type(strings))

#puede tener diferentes tipos de datos

#accediendo a valores de la tupla
print('0=>', numbers[0])
print('1=>', numbers[1])
print('2=>', numbers[2])
print('-1=>', numbers[-1])

#en una lista tenemos el CRUD
#con la tupla solo tenemos la declaracion, no la podemos modificar
#numbers.append(55)  #'AttributeError'
print(numbers)
#tampoco puedo modificar:
#numbers[1] = 85

#las tuplas son solo de lectura

#métodos de la tupla
#buscar:
print('zule is in index:' ,strings.index('juan'))

#contar un elemento
print(strings.count('sara'))

#podemos hacer transformaciones:
my_list = list(strings) #pasamos de tupla a list
print(type(my_list))
my_list.append('aleja')
print(my_list)

#cambiamos de lista a tupla
strings = tuple(my_list)
print(strings)
print(type(strings))

