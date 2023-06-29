# Comprehensions: List Comprehension

# Without list comprehension
numbers = []
for i in range(1, 11):
    numbers.append(i * 2)
    
print(numbers)

# With list comprehension
numbers = [i for i in range(1,11)]
print(numbers)

numbers_v2 = [i * 2 for i in range(1,11)]
print(numbers_v2)

# With list comprehension with condition
numbers_v3 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers_v3) # print numbers that are divisible by 2

# With list comprehension with condition but without list comprehension
numbers_v4 = []
for i in range(1,11):
    if i % 2 == 0:
        numbers_v4.append(i * 2)

print(numbers_v4)