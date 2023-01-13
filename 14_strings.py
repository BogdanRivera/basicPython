"""
Las cadenas de texto tienen algunas funciones para poder el tamaño, capitalizar la frase, etc. 
"""

text = "Ella sabe programar en Python"
'''
print("Javascript" in text) #Busca si en el texto está la palabra Javascript
print('Python' in text)
if 'Python' in text:
  print("ELEGISTE BIEN!!!")
else:
  print("También elegiste bien")
'''
size = len('Amor') #Verifica cuantos caracteres tiene la frase o palabra
print(size) #Imprime dicho numero
print(text)
print(text.upper()) #Pasa a mayúsculas

print(text.lower()) #Cambia a minúsculas

print(text.count('a')) #Cuenta cuantas letras 'a' tiene la frase

print(text.swapcase()) #Transforma las mayúsculas en minúsculas y viceversa

print(text.startswith('Ella')) #Pregunta si el texto inicia con algúna palabra
print(text.endswith('Rust'))#Pregunta si el texto termina con algúna palabra
print(text.replace("Python",'Go'))
#Cambia la primer palabra por la siguiente palabra

text_2 = 'Este es un titulo'
print(text_2)
print(text_2.capitalize()) #Pone la primer letra en mayúscula
print(text_2.title()) #Cada una de los inicios de palabra los pone con mayúscula
print(text_2.isdigit()) #Evalua si es un dígito
print("398".isdigit())







  
