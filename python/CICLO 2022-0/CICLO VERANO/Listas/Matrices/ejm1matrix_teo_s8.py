#El programa muestra el trabajo con una matriz de 3 x 5
#3 filas x 5 columnas
#Imprime la matriz, suma una columna, suma una fila
#Y finalmente suma todos los elementos de la matriz

matriz = [ [11, 12, 13, 14, 15 ],
          [21, 22, 23, 24, 25],
          [31, 32, 33, 34, 35]
        ]

for f in range(0,3,1):
   for c in range(0,5,1):
       print("%6d" %(matriz[f][c]),end="")
   print()
print()
print("Sumar los elemento de la columna 3")
suma =0
for f in range(3):
   suma = suma + matriz[f][3]
print("La suma de los elementos de la columna 3 es: ", suma)
print()
print("Suma los elementos de la fila 1: ")
suma = 0
for c in range(5):
   suma = suma + matriz[1][c]
print("La suma de los elementos de la fila 1 es: ", suma)
print()
print("Sumar todos los elementos de la matriz")
suma =0
for f in range(3):
   for c in range(5):
       suma = suma + matriz[f][c]
print("La suma de toda la matriz es : ", suma)
