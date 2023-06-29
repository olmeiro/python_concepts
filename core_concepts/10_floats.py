x :float = 3.3
print(f"x: {x}")
y = 1.1 + 2.2
print(f"y: {y}")
print(f"x == y: {x == y}")

#cómo comparar flotantes

#por strings: brusca
y_string = format(y, ".2g")
print("str => " , y_string)

print(y_string == str(x))

print("_" * 30)
#matematicamente:
print(x, y)
tolerance = 0.00001
print(abs(x - y) < tolerance)

print()
x = 3.3
print(x)
y = round((1.1 + 2.2),1) 
print(y)
print(x==y)