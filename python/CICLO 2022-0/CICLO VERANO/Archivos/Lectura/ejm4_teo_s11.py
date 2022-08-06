#El programa lee datos del archivo numeritos.txt y halla la suma de los números.

mifile = open("numeritos.txt","r")
suma = 0
unaLinea = mifile.readline()
while unaLinea!="":
    suma+=int(unaLinea)
    unaLinea=mifile.readline()
mifile.close()
print("La suma es: ",suma)
