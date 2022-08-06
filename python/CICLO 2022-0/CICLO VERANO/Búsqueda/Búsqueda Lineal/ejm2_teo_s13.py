
from random import randint


def busquedaLineal(lista, dato):
    for indice in range(len(lista)):
        if lista[indice] == dato:
            return True
    return False


#----------bloque principal
n = int(input("Numero de elementos: "))
lista = []
for elem in range(n):
    lista.append(randint(1, 99))
print(lista)
print("Ahora se busca un dato en la lista")
dato = int(input("Dato a buscar : "))
esta = busquedaLineal(lista, dato)
if esta:
    print("El dato se encuentra en la lista ")
else:
    print("El dato no se encuentra en la lista")
