numbers = [1,2,3,4]

numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

# Usando map y lambda functions:
numbers_v3 = map(lambda i: i *2, numbers)
print(numbers_v3) #regresa un iterable
#convertirmos a lista
numbers_v4 = list(numbers_v3)

#mas corto:
numbers_v5 = list(map(lambda i: i *2, numbers))
print(numbers_v5)

numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7,]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x,y: x + y, numbers_1, numbers_2))
print(result) #itera hasta la lista más pequeña.
