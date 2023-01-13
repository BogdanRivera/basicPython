"""
En este desafío vas a tener un código base el cual usa la función input para solicitar tu nombre, apellido y edad, tu reto es crear un formato usando un string que como resultado realice un print en la sección Console con el siguiente mensaje:

Fíjate que debes hacer un cálculo para la edad y calcular cuál será la edad en 10 años según el valor ingresado.
"""

name = input('¿Cuál es tu nombre? => ')
print(name)
last_name = input('¿Cuál es tu apellido? => ')
print(last_name)
age = input('¿Cuál es tu edad? => ')
print(age)
age = int(age)

template = f"Hola mi nombre es {name} {last_name}, tengo {age} años y en 10 años tendré {age+10}"
print(template)