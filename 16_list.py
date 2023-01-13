"""
Una lista puede tener múltiples valores. Esto puede visualizarse como una caja que contiene varios objetos. Se iteran y pueden ser cambiados en cualquier momento
"""


numbers = [1,2,3,4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes','play videogames']
print(tasks)

types = [1,True,'hola'] #Se pueden almacenar muchos datos
print(types) 

print(numbers[0])
print(tasks[0])
text = 'Hola'
#text[0] = 'W' #No se pueden modificar de esta manera en strings
tasks[0] = 'watch platzi courses'
print(tasks) #Si se puede actualizar en otro tipo de listas no en cadena

print(numbers[:3])
print(True in types)

