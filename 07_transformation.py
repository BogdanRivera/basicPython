"""
El uso de transformaciones es muy utilizado para poder usar distintos valores en un régimen específico. Por ejemplo podemos convertir un número para que Python lo interprete como una cadena en vez del mismo número, o convertir un flotante a entero y viceversa.
"""

name = "Bogdan"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Bogdan" + " Rivera")
print(10+20)
print("Bogdan "+ "12")

age = 23
print("Mi edad es "+ str(age))
#str() sirve para transformar un valor a tipo sting o con una f en antes del mensaje
print(f"Mi edad es {age}")

age = input('Escribe tu edad =>')
age = int(age) #int() transforma en un entero
age += 10
print(type(age))
print(f"Tu edad en 10 años será {age}")

#De otra manera
edad = int(input("Ingresa tu edad: "))
print("Edad en 10 años: ",edad+10)

