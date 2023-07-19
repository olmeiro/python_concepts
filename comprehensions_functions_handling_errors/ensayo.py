import copy

items = [
    {
        'product':'remera',
        'price':100,
    },
    {
        'product':'pantalon',
        'price':300,
    },
    {
        'product':'pantalon 2',
        'price':200,
    },
]

def add_campo_sum( item):
    item['taxes'] = item['price'] * .19
    return item

price = list(map(lambda item: item['price'], items))
print('ITEMS:::::',items)
print('PRICE:::::',price)

new_item = list(map(add_campo_sum,copy.deepcopy(items)))
print(f'Lista vieja \n{items}')
print(f'Lista nueva \n{new_item}')