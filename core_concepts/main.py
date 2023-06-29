# print("hola olme, bienvenido a Python");

# print(12 + 5)

# #comentario

# '''
# Comentario de varias lineas
# '''

# #type of variable
# age = 12
# print(type(age))

# is_single = False
# print(is_single)

# my_age = input('¿Cual es tu edad?')
# print('mi_age: ', my_age)
# print(type(my_age))

# #Strings in Python:

#Paper scissors stone:
# user_option = input("piedra - papel - tijera? => ")
# user_option = user_option.lower()
#computer_option = 'papel' #usemos tuplas

# import random

# options = ('piedra', 'papel', 'tijera')
# user_option = input("piedra - papel - tijera? => ")
# if not user_option in options:
#   print('option invalid')
# user_option = user_option.lower()
# computer_option = random.choice(options)

# print('User option =>', user_option)
# print('PC option=>', computer_option)

# if (user_option == computer_option):
#   print('Empate!')
# elif (user_option == 'piedra'):
#   if (computer_option == 'tijera'):
#     print('piedra wins tijera')
#     print('User won!')
#   else:
#     print('papel Wins piedra!')
#     print('Computer won!')
# elif user_option == 'papel':
#   if computer_option == 'piedra':
#     print('paper winst stone')
#     print('user wins!')
#   else:
#     print('scissors wins paper')
#     print('Computer wins')
# elif user_option == 'tijera':
#   if computer_option == 'papel':
#     print('scissors wins paper')
#     print('user wins!')
#   elif computer_option == 'piedra':
#     print('piedra wins tijera')
#     print('Computer wins!')

#usando ciclos:
import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
      print('esa opcion no es valida')
      continue

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1

    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break
