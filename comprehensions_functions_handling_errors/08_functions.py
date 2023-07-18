# Funciones python
print('Hola')

def my_print(text):
  print(text * 2)

my_print('Este es my texto')
my_print('Hola')

a = 10
b = 90

c = a + b

def suma(a, b):
  my_print(a + b)

suma(1 ,5) # 6
suma(10, 4) # 14

# Funciones return
def sum_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)

# Parámetros por defecto y múltiples return
def find_volume (length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

result, width, text = find_volume(width=10)
print(result[0])