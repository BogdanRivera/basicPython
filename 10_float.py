"""
Los números flotantes tienen algunos problemas con los decimales, por lo que es necesario realizar una pequeña transformación de formato para lograr comparar dos de ellos. 
"""

x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x==y)
#Para solucionar esto la y se pasa a string.
y_str = format(y,".2")#Unicamente se quiere dos dígitos
print('str =>>',y_str)
print(y_str == str(x))

#De forma matemática
print('*'*10)

print(y,x)

tolerance = 0.0001
print(abs(x-y) < tolerance)
