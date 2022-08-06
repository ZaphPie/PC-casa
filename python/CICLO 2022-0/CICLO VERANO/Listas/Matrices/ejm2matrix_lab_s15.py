"""
1. Total de medallas obtenidas por China
2. Total de medallas de oro
3. Total de medallas de toda la tabla
4. El país que obtuvo menor cantidad de medallas de plata
"""
medallero = [
              ["Estados Unidos",   1022,   794,  704],
              ["Unión Soviética",   395,   319,  296],
              ["Reino Unido",       263,   295,  289],
              ["China",             227,   163,  153],
              ["Alemania",          219,   246,  269]
    ]

#imprimir la matriz
filas = len(medallero)
col = len(medallero[0])

for f in range(filas):
    print("%-20s" % (medallero[f][0]),end="") #anulamos el cambio de linea
    for c in range(1,col):
        print("%6d"%(medallero[f][c]),end="")
    print()
#---------------total de medallas de China----------------
print()
suma =0
for c in range(1,col,1):
    suma+=medallero[3][c]
print("La cantidad de medallas de China es:", suma)
#----------medallas de oro
print()
for f in range(filas):
    suma+=medallero[f][1]
print("El total de medallas de oro es: ", suma)
#------------total de medallas
print()
suma =0
for f in range(filas):
    for c in range(1,col, 1):
        suma+=medallero[f][c]
print("El total de medallas de toda la tabla es: ", suma)
#--------el país que tiene la menor cantidad de medallas de plata
print()
elMenor = medallero[0][2]
posDelMenor=0
for f in range(1,filas,1):
    if medallero[f][2]<elMenor:
        elMenor=medallero[f][2]
        posDelMenor =f
print("El país que tiene la menor cantidad de medallas de plata es:",medallero[posDelMenor][0])