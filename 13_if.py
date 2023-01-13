"""
Las condicionales If funcionan mucho para poder decidir dos caminos de acuerdo a una condición dada. Esto se lee como: si pasa esto realizamos esto. En otro caso tomamos otro camino. 
"""


if True:
  print('Debería ejecutarse')
if False:
  print('Nunca se ejecuta')

pet = input('¿Cuál es tu mascota favorita?')
if pet== 'perro':
  print("Tienes buen gusto")
elif pet=='gato':
  print('Espero que tengas suerte')
elif pet=='pez':
  print("Eres lo máximo")
else:
  print("No tienes una mascota interesante")

stock = int(input('Digita el stock =>'))
if stock >=100 and stock <= 1000: 
  print('El stock es correcto')
else:
  print("El stock es incorrecto")

#Evaluación si un número es par o impar

num = int(input("Ingresa un número: "))
if (num%2)==0:
  print("Es un número par")
else: 
  print("Es un número impar")


  