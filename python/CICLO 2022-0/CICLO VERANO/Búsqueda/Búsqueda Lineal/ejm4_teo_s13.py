#Desarrolle un programa que permita generar una lista con valores aleatorios y luego permita formar una nueva lista con todas las posiciones en que el dato aparece en la lista. Si no existe la lista estará vacía.
from random import randint


def hallaPosiciones(lista, numero):
    nl = []
    for indice in range(len(lista)):
        if lista[indice] == numero:
            nl.append(indice)
    return nl


#--------------bloque principal
ne = int(input("Numero de elementos : "))
lista = []
for i in range(ne):
    lista.append(randint(1, 99))
print(lista)
print("Buscaremos un dato en la lista")
numero = int(input("Ingrese dato a buscar:"))
listadePosiciones = hallaPosiciones(lista, numero)
if len(listadePosiciones) > 0:
    print("El dato se encuentra en estas posiciones")
    print(listadePosiciones)
else:
    print("No existen ocurrencias del dato en la lista")
