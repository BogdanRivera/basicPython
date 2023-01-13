"""
El indexado sirve para recorrer una lista, conjunto o tupla de una manera mas sencilla sin tener que recurrir al for. La posición comienza desde 0 que es el primer valor de dichos elementos
"""

text = "Ella sabe python"
print(text[0])
print(text[1])
#print(text[999])
size = len(text)
print(text[size-1])
print(text[-1]) #Empieza a contar en la última posición


#Slicing: Se pueden sacar ciertos rangos de la frase
print(text[0:5]) 
print(text[10:16])
print(text[:10]) #Asume que toma el inicio hasta el 10
print(text[5:-1]) #No toma todos los valores
print(text[5:]) #Va desde 5 hasta el final
print(text[:]) #Imprime todos los valores
print(text[10:16:1]) #Saltos a partir del string
print(text[10:16:2])
print(text[::2]) #Va desde el inicio hasta el final con saltos de dos
