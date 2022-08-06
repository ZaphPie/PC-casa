#--------------------------
#Dato de entrada: Filas, col (int)
#Dato de salida: imprimir la matriz
#--------------------------

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

def leerDatos(mat):
   filas =  len(mat)
   col   = len(mat[0])
   for f in range(filas):
       for c in range(col):
           dato = int(input("mat[%d][%d]= " % (f,c)))
           mat[f][c]=dato


#-----bloque principal
filas = int(input("Numero de filas: "))
col   = int(input("Numero de columnas: "))
matriz = dimensionaMatriz(filas, col)
leerDatos(matriz)
imprimirMatriz(matriz)

