"""
Los diccionarios son ampliamente utilizados para asignar un alias a un valor, tal como Aguinaldo:2000. Esta notacion permite guardar un valor para cada item. Se pueden guardar múltiples diccionarios en listas o en tuplas.
"""

my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Bogdan',
  'last_name' : 'Rivera', 
  'age': 24  
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age')) #Obtiene el elemento y si no existe lo puede manejar sin problemas
print(my_dict.get('unvalor')) 

print('avion' in my_dict)
print('otroqueno' in my_dict)
