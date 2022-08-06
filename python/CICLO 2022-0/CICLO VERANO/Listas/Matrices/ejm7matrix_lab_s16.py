"""
Desarrollar un programa que permita leer el orden de una matriz
, luego genere una matriz con datos aleatorios y la imprima.
 Posteriormente genere una segunda matriz que va a tener el número 1
 si el dato de la misma posicion en la matriz original es par
 o tener el número 0 si el dato de la misma posición en la matriz original es impar.

"""

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

def verificarMatriz(m1,m2):
    filas =len(m1)
    col =len(m1[0])
    for f in range(filas):
        for c in range(col):
            if m1[f][c]%2 ==0:
                m2 [f][c]=1
            else:
                m2[f][c]=0
#-----------bloque principal
filas = int(input("Número de filas: "))
col = int(input("Número de columnas: "))
m1 = dimensionaMatriz(filas,col)
llenarDatos(m1)
imprimirMatriz(m1)
print()
m2 =dimensionaMatriz(filas,col)
verificarMatriz(m1,m2)
imprimirMatriz(m2)