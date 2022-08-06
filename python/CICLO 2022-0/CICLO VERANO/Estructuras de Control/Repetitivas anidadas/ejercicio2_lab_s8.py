#EJERCICIO 6 de la GUÍA:
#Dato de entrada: filas (int) filas>=1
#Dato de salida: Triángulo con *

filas = int(input("Filas: "))
while filas<1:
    filas = int(input("Filas: "))
casteriscos=1
for cf in range(1,filas+1,1):
    print((filas-cf)*" "+"*"*casteriscos)
    casteriscos=casteriscos+2

