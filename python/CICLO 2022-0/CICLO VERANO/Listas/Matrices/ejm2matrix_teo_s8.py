#--------------------------------------------------------------------------------------
#Desarrollar un programa que pidad como datos el orden de una matriz
#Y el programa forme una matriz con datos aleatorios y los muestre en la pantalla
#---------------------------------------------------------------------------------------
from random import randint

def imprimirMatriz(mat):
    filas = len(mat)
    col = len(mat[0])
    for f in range(filas):
        for c in range(col):
            print("%7d"% (mat[f][c]),end="")
        print()

def llenarDatos(matriz):
    filas = len(matriz)
    col = len(matriz[0])
    for f in range(filas):
        for c in range(col):
            matriz[f][c]=randint(1,50)



#-------------------------------------
filas = int(input("Número de filas: "))
col = int(input("Número de columnas: "))
#-------------dimensionamos la matriz
matriz = []
for f in range(filas):
    unaFila = [0]*col
    matriz.append(unaFila)
imprimirMatriz(matriz)

print()
llenarDatos(matriz)
imprimirMatriz(matriz)