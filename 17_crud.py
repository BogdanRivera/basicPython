#CRUD Create, Read, Update and Delete
"""
Las funciones principales de las listas pueden modificar cualquier elemento. Basta con usar algunos métodos o simplemente realizar una suma sencilla
"""

numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0,'hola')
print(numbers)

numbers.insert(3,'change')
print(numbers)

task = ['todo 1','todo 2','todo 3']
new_list = numbers+task
print(new_list)

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1,4,5,3]
print(numbers_a.sort()) #Ordena los numeros

strings = ['re','ab','ed']
strings.sort()
print(strings)


