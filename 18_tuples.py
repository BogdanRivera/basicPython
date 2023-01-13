#En la lista teniamos un CRUD
#Aquí solo se hace la declaración pero no se pueden modificar
#Una vez declarada unicamente deja imprimirla
"""
Al igual que una lista, los elementos pueden visualizarse de una manera similar, con la diferencia de que estas no pueden modificarse de ninguna forma. Una vez creadas solo se pueden hacer métodos de visualización
"""
numbers = (1,2,3,5)
strings = ('Bogdan','Paco','Zule','nico')
print(numbers)
print('0 => ',numbers[0])
print('-1 => ',numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#numbers.append(10)

print(strings)
print(strings.index('Zule'))
print(strings.count('nico')) #Cuenta cuantas veces se encuentra ese elemento en la tupla

my_list = list(strings) #Pasamos de tupla a lista
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

