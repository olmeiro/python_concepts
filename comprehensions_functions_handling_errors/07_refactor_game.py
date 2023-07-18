import random

#choose options:
def choose_options():
  options = ('piedra', 'papel', 'tijera')

  user_option = input('piedra, papel o tijera =>').lower()
  
  if not user_option in options:
    print('esa opción no es válida')
    return None, None
    #continue
  
  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)

  return user_option, computer_option

def check_rules(user_option, computer_option,user_wins, computer_wins):
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
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if computer_wins == 2:
    print('El ganador es la computadora')
    exit()

  if user_wins == 2:
    print('El ganador es el usuario')
    exit()


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    winner =  check_winner(user_wins, computer_wins)
    
  return winner

run_game()
      
# execute program in cmd: python 07_refactor_game.py