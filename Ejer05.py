"""
En este desafío tienes una lista de números positivos y negativos, declarada como my_list, tu reto es aplicar un ciclo para seleccionar los números positivos de my_list y agregarlos a new_list.

Recuerda usar al final usar la función print para imprimir los valores de new_list.
"""

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇

for i in my_list:
  if i>0:
    new_list.append(i)
  
print(new_list)