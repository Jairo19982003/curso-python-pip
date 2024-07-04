import random

options = ('piedra', 'papel', 'tijera')


def choose_options():
    user_option =input('piedra, papel o tijera => ')
    user_option = user_option.lower()
    
    if not user_option in options:
      print('Esa opcion no es valida.')
     # continue
      return None, None
      
    computer_option = random.choice(options)
    
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_score, computer_score):
  if user_option == computer_option:
     print('Empate')
     
  elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera.')
        print('Ganaste')
        user_score += 1
        
    else:
        print('papel gana a tiedra.')
        print('perdiste.')
        computer_score += 1
        
  elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel le gana a piedra.')
        print('Ganaste')
        user_score += 1
        
    else:
        print('tijera gana a papel')
        print('Perdiste')
        computer_score += 1

  elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera le gana a papel.')
        print('Ganaste')
        user_score += 1
        
    else:
        print('piedra gana a tijera ')
        print('Perdiste')
        computer_score += 1
      
  return user_score, computer_score
        

        
def run_game():
  computer_score = 0
  user_score = 0
  rounds = 1
  
  while True:
    print('=' *10)
    print('Round', rounds)
    print('=' *10)

    print('computer_score', computer_score)
    print('user_score', user_score)

    rounds += 1

    user_option, computer_option = choose_options() 
    
    user_score, computer_score =   check_rules(user_option, computer_option, user_score, computer_score)


    if computer_score == 2:
        print("La computadora gano.")
        break

    if user_score == 2:
        print("El usuario gano.")
        break

run_game()