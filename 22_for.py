"""
Las funciones for también son métodos de control y este permite hacer un seguimiento a través de ciertas condiciones, iterando normalmente una lista o diccionario. 
"""

"""
for element in range(1,21):
  print(element)
"""

my_list = [23,45,67,89,43]

for i in my_list:
  print(i)

my_tuple = ('Bogdan','Juli','Nico')
for element in my_tuple:
  print(element)


product = {
  'name':'camisa',
  'price':100,
  'stock':89
}

for key in product:
  print(key,'=> ', product[key])

for key, value in product.items():
  print(key, '=>',value)

people = [
  {
    'name':'nico',
    'age':24
  },
  {
    'name':'zule',
    'age':45
  },
  {
    'name':'santi',
    'age':4
  }
]

for person in people:
  print('name =>',person['name'])

