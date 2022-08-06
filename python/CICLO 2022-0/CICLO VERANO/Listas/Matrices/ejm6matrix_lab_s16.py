"""
Desarrollar un programa que permita leer como dato el orden de una matriz
y el programa permita generar dos matrices con datos aleatorios y
luego halla la matriz suma.

"""
#------------------------
#Input: filas, col (int)
#Output: matrizSuma
#-----------------------
from random import randint

def imprimirMatriz(m):
   filas = len(m)
   col   = len(m[0])
   for f in range(filas):
       for c in range(col):
           print("%5d" % (m[f][c]), end="")
       print()

def dimensionaMatriz(filas, col):
   matriz = []
   for f in range(filas):
       unaFila = [0] * col
       matriz.append(unaFila)
   return matriz

def llenarDatos(mat):
    filas = len(mat)
    col = len(mat[0])
    for f in range(filas):
        for c in range(col):
            mat[f][c]=randint(1,50)

def sumarMatrices(m1,m2):
    filas = len(m1)
    col = len(m1[0])
    ms = dimensionaMatriz(filas,col)
    for f in range(filas):
        for c in range(col):
            ms[f][c]=m1[f][c]+m2[f][c]
    return ms
#-----------bloque principal
filas = int(input("Número de filas: "))
col = int(input("Número de columnas: "))
m1 = dimensionaMatriz(filas,col)
llenarDatos(m1)
imprimirMatriz(m1)
print()
m2=dimensionaMatriz(filas,col)
llenarDatos(m2)
imprimirMatriz(m2)
print()
matrizSuma=sumarMatrices(m1,m2)
imprimirMatriz(matrizSuma)