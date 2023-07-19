# map con diccionarios:
items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'jeans',
        'price': 120
    },
    {
        'product': 'tennis',
        'price': 160
    },
]

# como transformamos esto a una lista de precios, solo precios:
prices = list(map(lambda item: item['price'], items))
print(items) #map no muta el original
print(prices)

# Agregar un nuevo atributo de impuestos (taxes) a los elementos:
# def add_taxes(item):
#     item['taxes'] = item['price'] * 0.19  #modificamos la referencia compartida
#     return item

#new_items = list(map(add_taxes, items)) #aqui mutamos el array original y map no respeta la inmutabilidad. con primitivos calculamos un nuevo valor y lo asignamos al array, pero con diccionarios no se asigna como un nuevo valor sino como una referencia en memoria por lo que se modifican los dos arrays que comparten la referencia en memoria.
# print(new_items)
# print(items) #hemos mutado el original por referencia en memoria en add_taxes

# arreglemos la referencia en memoria 
def add_taxes_inmutable(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

new_items = list(map(add_taxes_inmutable, items))
print('items', items) #aqui respetamos la inmutabilidad
print('new_items', new_items)
