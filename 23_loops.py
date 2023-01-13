"""
Para la visualización de una matriz es necesario utilizar dos ciclos for, donde se leen primero las filas y posteriormente las columnas
"""

matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matriz[0])

for row in matriz:
  print(row)
  for column in row:
    print(column)


