"""
Considerando la siguiente matriz:
Imprima la matriz
Sume los elementos de la columna cuyo índice es 3
Sume los elementos de la fila cuyo índice es 2
Sume los elementos  de toda la matriz.

"""
matriz = [
                [  1,    2,    3,    4,   5 ],
                [ 10,  20,  30,  40, 50],
                [ 51,  52,  53,  54, 55]
             ]

#----------Imprimir matriz
filas =len(matriz) #cantidad de filas
col = len(matriz[0]) #cantidad de columnas

for f in range(0,filas,1):
    for c in range(0,col,1):
        print("%6d" %(matriz[f][c]),end="") #anular el cambio de linea
    print()

#------------Se suma los elementos de la columna 3
suma = 0
for f in range(filas):
    suma +=matriz[f][3]
print("La suma de los elementos de la columna 3 es: ",suma)
#-----------------sumar los elementos de la fila 2----------------
print()
suma = 0
for c in range(col):
    suma +=matriz[2][c]
print("La suma de los elementos de la fila 2 es: ",suma)
#----------------Se suma todos los elementos de la matriz
print()
suma =0
for c in range(col):
    for f in range(filas):
        suma +=matriz[f][c]
print("La suma de todos los elementos de la matriz es: ",suma)