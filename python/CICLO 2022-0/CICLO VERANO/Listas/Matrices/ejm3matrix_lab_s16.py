"""
Desarrolle un programa que permita generar una matriz de 3 x 7,
con datos aleatorios entre 1 y 50 y la imprima.
"""
from random import randint

def imprimirMatriz(m):
    filas = len(m)
    col= len(m[0])
    for f in range(filas):
        for c in range(col):
            print("%5d"%(m[f][c]),end="")
        print()






#------------------------
# CREAR MATRIZ DE 3x7
m = []
for f in range(3):
    unafila = [0]*7
    m.append(unafila)
print(m)
#----Llenamos la matriz con valores aleatorios
for f in range(3):
    for c in range(7):
        m[f][c]=randint(1,50)
imprimirMatriz(m)