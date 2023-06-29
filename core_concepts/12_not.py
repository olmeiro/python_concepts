print(not True)
print(not False)
print()

#not and
print("AND")
print('True and True =>', not(True and True))
print('True and False =>', not(True and False))
print('False and True =>', not(False and True))
print('False and False =>', not(False and False))

print()
stock = input("Ingrese el número de stock => ")
stock = int(stock)
print(not(stock >= 100 and stock <= 1000))