"""
Ejemplo del uso de un diccionario
"""


person = {
  'name':'Bogdan',
  'last_name':'Rivera',
  'langs':['python','javascript'],
  'age':24
}

print(person)
#Modificar el diccionario
person['name'] = 'santi'
person['age'] -= 10
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')

print(person)

print('Items =>',person.items()) #Pares
print('Keys =>',person.keys()) #Atributos
print('Values =>',person.values()) #Valores 


