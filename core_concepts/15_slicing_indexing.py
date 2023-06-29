#indexing: indicador de posicion
text = 'Ella sabe Python'
print(text[0])
print(text[-1]) #ültimo caracter
#print(text[999]) #error
size = len(text)
# print(text[size]) #error by size array
print(text[size - 1]) #error by size array

#slicing:
print(text[0:6]) #substring desde 0 hasta el 5
print(text[10:16])
print(text[0:10]) #inicio al 10
print(text[:10]) #inicio al 10

print(text[5:-1]) #desde el 5 hasta el último sin incluirlo
print(text[5:]) #hasta el final

#saltos   
print(text[10:16:1]) #saltando caracteres de a 1
print(text[10:16:2]) #saltando caracteres de a 2

print(text[::2]) #inicio-final saltando de a dos elementos