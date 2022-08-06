a = int(input("Ingrese un número 1: "))
b = int(input("Ingrese un número 2: "))
c = int(input("Ingrese un número 3: "))
d = int(input("Ingrese un número 4: "))
contpar=0

if a%2==0:
    contpar=contpar+1
elif b%2==0:
    contpar=contpar+1
elif c%2==0:
    contpar=contpar+1
elif d%2==0:
    contpar=contpar+1
if contpar ==0:
    print("Respuesta: Cero pares")
if contpar ==1:
    print("Respuesta: Un par")
if contpar ==2:
    print("Respuesta: Dos pares")
if contpar ==3:
    print("Respuesta: Tres pares")
if contpar ==4:
    print("Respuesta: Cuatro pares")

