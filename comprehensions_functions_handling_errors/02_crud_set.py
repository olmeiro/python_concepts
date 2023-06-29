set_countries = {'colombia', 'peru', 'ecuador', 'argentina', 'chile', 'venezuela', 'brasil', 'bolivia', 'uruguay', 'paraguay'}

# size 
print(len(set_countries))

print('Colombia' in set_countries)
print('colombia' in set_countries)

# add
set_countries.add('mexico')
print(set_countries)

# update
set_countries.update(['cuba', 'puerto rico', 'costa rica'])
print(set_countries)

# remove: produce error if not exists
set_countries.remove('cuba')
print(set_countries)

# discard: remove if exists and avoid error if not exists
set_countries.discard('cuba')
print(set_countries)

# pop: remove random element
set_countries.pop() # remove random element
print(set_countries)

# clear
set_countries.clear()
print(set_countries)