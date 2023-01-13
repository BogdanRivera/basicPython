"""
Los operadores while es un ciclo de control que permite la repetición continua de algúna acción hasta que rompa cierta condición. Una vez rota dicha condición el ciclo ya no continua y sigue con las siguientes instrucciones
"""

'''
while True:
  print("Se ejecuta")

'''

counter = 0
"""
while counter < 10:
  counter += 1
  print(counter)
"""
"""
counter = 0
while counter<20:
  counter += 1
  if counter == 15:
    break #Rompe el ciclo 
  print(counter)
"""
while counter<20:
  counter += 1
  if counter < 15:
    continue #Se salta las instrucciones y continua con el ciclo 
  print(counter)


  