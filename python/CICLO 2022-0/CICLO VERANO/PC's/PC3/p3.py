#3.
from random import randint

def imprimirMatriz(mat):
    filas = len(mat)
    col = len(mat[0])
    for f in range(filas):
        for c in range(col):
            print("%7d" % (mat[f][c]), end="")
        print()


def llenarDatos(matriz):
    filas = len(matriz)
    col = len(matriz[0])
    for f in range(filas):
        for c in range(col):
            matriz[f][c] = randint(0, 9)


def dimensionarMatriz(filas, col):
    matriz = []
    for f in range(filas):
        unaFila = [0]*col
        matriz.append(unaFila)
    return matriz


filas = int(input("Filas: "))
col = int(input("Columnas: "))
m1 = dimensionarMatriz(filas, col)
llenarDatos(m1)
imprimirMatriz(m1)
print()
frecuencias={}
for f in range(filas):
    for c in range(col):
        if m1[f][c] not in frecuencias:
            frecuencias[m1[f][c]] =1
        else:
            frecuencias[m1[f][c]]=frecuencias[m1[f][c]]+1
print(frecuencias)