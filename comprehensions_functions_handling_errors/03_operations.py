set_a = {'col', 'mex', 'bol'}
set_b = {'bol', 'pe'}

# union: elements that are in either set
set_c = set_a.union(set_b)
print(set_c)

# unio with math operator
set_d = set_a | set_b

# intersection: elements that are in both sets
set_e = set_a.intersection(set_b)
print(set_e)

# intersection with math operator
set_f = set_a & set_b
print(set_f)

# difference: elements that are in one set but not the other
set_g = set_a.difference(set_b)
print(set_g)

# difference with math operator
set_h = set_a - set_b
print(set_h)

# symmetric difference: elements that are in one set or the other, but not both

set_i = set_a.symmetric_difference(set_b)
print(set_i)

# symmetric difference with math operator
set_j = set_a ^ set_b
print(set_j)

#delete duplicates
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set = countries | northAm | centralAm | southAm

print(new_set)
