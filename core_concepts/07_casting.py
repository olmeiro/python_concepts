name = 'OLmeiro'
print(type(name))

#transformación dinácompile
name = 12
print(type(name))

print("Olmeiro" + " Orozco") #concatena

print(10 + 20) #suma
#print('Olme' + 12) #error

age = 30
#print("mi Edad es: " + age) #error

#casting:
print("mi Edad es: " + str(age))

#casting automatico
print(f"mi edad es {age}")

age2 = input("tu edad:::")
print(type(age2))
age2 = int(age2)
print(f'tu edad en 10 años sera {age2 + 10}')