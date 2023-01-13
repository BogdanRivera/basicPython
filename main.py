"""
Creación básica de un juego de piedra, papel o tijera. En este caso el conteo se hace a dos partidas ganadas. Una vez que haya un ganador el juego se cierra
Realizad por: Bogdan Kaleb García Rivera
"""


import random 

options = ('piedra','papel','tijera')
rounds = 1
computer_wins = 0
user_wins = 0
while True:
  print('*'*10)
  print('ROUND ',rounds)
  print('*'*10)

  print('computer_wins: ',computer_wins)
  print('user_wins: ',user_wins)
  
  
  user_option = input("piedra, papel o tijera: ").lower()
  rounds+=1
  
  if not user_option in options:
    print('Esa opción no es válida')
    continue
  computer_option = random.choice(options)
  
  print('User option => ',user_option)
  print('Computer option =>',computer_option)
  
  
  if user_option == computer_option: 
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('user ganó!')
      user_wins += 1
    else:
      print("Papel gana a piedra")
      print('Computer ganó!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option=='piedra':
      print("Papel gana a piedra")
      print('User ganó!')
      user_wins += 1
    else:
      print("Tijera gana a papel")
      print("Computer ganó!")
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option =='papel':
      print("Tijera gana papel")
      print("User ganó!")
      user_wins += 1
    else:
      print("Piedra gana a tijera")
      print("Computer ganó")
      computers_wins += 1
  else:
    print("Opción no valida")

  if computer_wins == 2:
    print("El computador es el ganador")
    break
  if user_wins == 2:
    print("El usuario es el ganador")
    break




  
    
  
    




