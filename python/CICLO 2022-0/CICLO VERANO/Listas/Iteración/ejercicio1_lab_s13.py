#Input: Número de elementos (int) , dato (int)
#Output: Verificar si el dato esta en la lista
#        Contar las veces que el dato esta en la lista
#        nuevaLista con las posiciones del dato en la l
from random import randint

def buscar(dato,lista):
    for i in range(0,len(lista),1):
        if dato==lista[i]:
            return i
    return -1
def cuentaOcurrencias(dato,lista):
    cont =0
    for elemento in lista:
        if dato ==elemento:
            cont +=1
    return cont
def listadePosiciones(dato,lista):
   nuevaLista =[]
   for i  in range(0, len(lista),1):
       if lista[i] ==dato:
           nuevaLista.append(i)
   return nuevaLista
#-----------------------------
ne = int(input("Número de elementos: "))
lista = []
for cont in range(1,ne+1,1):
    lista.append(randint(1,20))
print(lista)
print()
datoaBuscar = int(input("Dato a buscar: "))
pos = buscar(datoaBuscar, lista)
if pos != -1 :
    print("El dato está en la posición: ", pos)
else:
    print("El dato no está!")
print("")
print("Ahora hallamos las veces que un dato está en la lista")
print("El dato está", cuentaOcurrencias(datoaBuscar,lista),"veces")
print("Las posiciones en que el dato está en la misma lista son: ", listadePosiciones(datoaBuscar,lista))