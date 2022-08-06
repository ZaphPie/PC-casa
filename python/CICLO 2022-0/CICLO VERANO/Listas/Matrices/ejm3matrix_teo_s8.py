#----------------------------------------------------------------
#Desarrolle un programa que permita leer el orden de una matriz
#Luego el programa forme dos matrices con datos aleatorios
#Finalmente hallar la suma de las matrices
#----------------------------------------------------------------
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

def dimensionarMatriz(filas,col):
    matriz=[]
    for f in range(filas):
        unaFila= [0]*col
        matriz.append(unaFila)
    return matriz

def sumarMatrices(m1,m2):
    filas =len(m1)
    col = len(m1[0])
    nuevaMatriz=dimensionarMatriz(filas,col)
    for f in range(filas):
        for c in range(col):
            nuevaMatriz[f][c]=m1[f][c]+m2[f][c]
    return nuevaMatriz
#-------------------------------------
filas = int(input("Número de filas: "))
col = int(input("Número de columnas: "))
#-------------dimensionamos la matriz
m1 = dimensionarMatriz(filas, col)
llenarDatos(m1)
imprimirMatriz(m1)
print()
m2 = dimensionarMatriz(filas,col)
llenarDatos(m2)
imprimirMatriz(m2)
print()
m3=sumarMatrices(m1,m2)
imprimirMatriz(m3)