"""
El uso de variables dependerá del tipo de variable y su valor
Existen númericas, de cadenas, conjuntos, listas,etc. 
"""

print("Hola, vars")
#Esto es una variable
my_name = "Bogdan"

print(my_name)

#Esto es una variable con un número
my_age = 23
print(my_age)

my_name = "Santiago"
print("Aquí hice un cambio",my_name)
# Función input
my_name = input("¿Cual es tú nombre?")
print("Usando input",my_name)

my_age = input("¿Cuál es tu edad?")
print("Usando input", my_age)

#Programa que da la bienvenida
print(f"Hola { my_name},bienvenido al mundo de la programación :3")
