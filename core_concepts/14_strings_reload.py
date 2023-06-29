#Strings recargado

texto = 'Ella sabe programar en Python'
print('Javascript' in texto)
print('Python' in texto)

if 'Python' in texto:
  print('Si señores')
else:
  print('Excelente bro. js mmm!')

#tamaño string: cuenta spaces
size = len('aprendiendo ')
print(size)
print('*' * 20)
#métodos:
print(texto)
print(texto.upper())
print(texto.lower())
print(texto.count('a'))

print(texto.swapcase())
print(texto.startswith('Ella'))
print(texto.endswith('Ella'))

#replace:
print(texto.replace('Python', 'Go'))

texto_2= 'este es un título'
print(texto_2)
print(texto_2.capitalize())
print(texto_2.title())
print(texto_2.isdigit())
print("398".isdigit())