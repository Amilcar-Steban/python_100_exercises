"""
[
    [0, 0, 0], 
    [0, 0, 1], 
    [0, 1, 0], 
    [1, 0, 0], 
    [1, 1, 1]

]

"""
import math

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# create grid empty
grid = []
facto = math.factorial(3)+1
fila = []  # make new file empty
if x >=0 and y >=0 and z >=0:
    for i in range(facto):
            for j in range(facto): 
                    for k in range(facto):
                        if i <= x and j <= y and k <= z and (i+j+k) !=n:
                            valor = [i, j, k]
                            fila.append(valor)
    grid.append(fila)

# Imprimir el grid
for fila in grid:
    print(fila)

