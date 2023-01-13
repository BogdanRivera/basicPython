"""
En este desafío tienes un diccionario que representa los datos de una persona y está declarada como person y tu reto es realizar las siguientes tareas en orden:

Agregar un nuevo atributo llamado twitter con el valor @nicobytes
Actualizar el atributo name con el valor Felipe
Eliminar el atributo age.
Imprimir una lista con las llaves del diccionario.
Imprimir una lista con los valores del diccionario.
"""

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
person.pop('age')
print(list(person.keys()))
print(list(person.values()))
