"""
El uso de Strings es apliamente utilizado en cualquier programa.
Este tiene mucho uso en varias aplicaciones
"""

#Clase de strings 
name = 'Bogdan'
last_name = "Rivera"
edad = 23
print(name)
print(last_name)

full_name = name + " "+ last_name
print(full_name)

quote = "I'm Bogdan" #Para hacer esto es recomendable usar comillas dobles, esto debido a que si tuvieramos comilla simple tendríamos un error debido a que Python reconocería que acabas de cerrar la frase
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#Formato
template = "Hola, mi nombre es "+name+" y mi apellido es "+last_name
print('v1:',template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name,last_name)
print('v2:',template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3:',template)

#Utilizando la tercera variable
persona = f"Hola, mi nombre es {name} {last_name} y mi edad es {edad}"
print(persona)
