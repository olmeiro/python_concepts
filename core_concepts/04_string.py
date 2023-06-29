print("hola")
name = 'olmeiro'
last_name = 'orozco'
#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name

print(template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('v2', template2)

template3 = f"Hola, mi nombre es {name} y mi apellido es {last_name}"

print("v3", template3)