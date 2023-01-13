"""
Las variables lógicas surgen de la electrónica digital. A partir de ellas se pueden visualizar las AND, OR, XOR, NOT, etc. 
"""
# and
print("AND")
print('True and True =>',True and True)
print('True and False =>',True and False)
print('False and True =>',False and True)
print('False and False =>',False and False)
print (10>5 and 5<10)
print (10>5 and 5>10)

stock = int(input('Ingrese el número de stock=>'))

print(stock>=100 and stock <=1000)

# Or
print("OR")
print('True or True =>',True or True)
print('True or False =>',True or False)
print('False or True =>',False or True)
print('False or False =>',False or False)
print (10>5 or 5<10)
print (10>5 or 5>10)

role= input('Digita el rol => ')
print(role == 'admin' or role=='seller')

