'''Tipos de datos primitivos
Integers: números Enteros
Floats: números de punto flotante (decimales)
Strings: cadena de caracteres (texto)
Boolean: boolenaos (Verdadero o Falso)
Tipos de dato adicionales
Datos en texto: str
Datos numéricos: int, float, complex
Datos en secuencia: list, tuple, range
Datos de mapeo: dict
Set Types: set, frozenset
Datos booleanos: bool
Datos binarios: bytes, bytearray, memoryview
'''

#String  
my_name = "Nicolas"
my_name = 'Bogdan'
print('my_name =>',my_name)
print(type(my_name)) #Muestra el tipo de variable 

#int
my_age = 23
print('My_age =>',my_age)
print(type(my_age))

#Boolean
is_single = False
print("is_single=>",is_single)
print(type(is_single))

#inputs
my_age = input('¿Cuál es tu edad?')
print('My_age =>',my_age)
print(type(my_age)) #Los inputs siempre se pasan como de tipo String


