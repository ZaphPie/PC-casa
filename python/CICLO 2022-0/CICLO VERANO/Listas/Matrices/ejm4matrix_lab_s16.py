"""
Ahora genere una matriz de 10 x 4
con datos aleatorios entre 1 y 100
y el programa imprima el mayor dato y su posición
"""

from random import randint

def llenarMatriz(matriz):
    filas = len(matriz)
    col = len(matriz[0])
    for f in range(filas):
        for c in range(col):
            matriz[f][c]=randint(1,100)

def imprimirMatriz(m):
    filas =len(m)
    col = len(m[0])
    for f in range(filas):
        for c in range(col):
            print("%5d"%(m[f][c]),end ="")
        print()

def HallarMayorysuPosicion(mat):
    filas = len(mat)
    col = len(mat[0])
    mayor = mat[0][0]
    posF = 0
    posC = 0
    for f in range(filas):
        for c in range(col):
            if mat[f][c]>mayor:
                mayor=mat[f][c]
                posF=f
                posC=c
    return mayor,posF,posC


#-----------------------------------
filas = 10
col = 4
mat=[]
for f in range(filas):
    unaFila=[0]*col
    mat.append(unaFila)
#-----llenamos la matriz con datos aleatorios
llenarMatriz(mat)
imprimirMatriz(mat)
elMayor, posFilas, posCol = HallarMayorysuPosicion(mat)
print()
print("El dato mayor es:", elMayor)
print()
print("Esta en la fila:",posFilas,"y en la columna : ",posCol)