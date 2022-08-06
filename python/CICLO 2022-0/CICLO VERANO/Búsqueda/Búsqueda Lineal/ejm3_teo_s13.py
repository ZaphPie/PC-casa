from random import randint


def busquedaLineal(lista, dato):
    #-- retorna el indice si no encuentra y -1 si no lo encuentra
    for indice in range(len(lista)):
        if lista[indice] == dato:
            return indice
    return -1


#----------bloque principal
n = int(input("Numero de elementos: "))
lista = []
for elem in range(n):
    lista.append(randint(1, 99))
print(lista)
print("Ahora se busca un dato en la lista")
dato = int(input("Dato a buscar : "))
posicion = busquedaLineal(lista, dato)
if posicion != -1:
    print("El dato se encuentra en la lista en la posicion : ", posicion)
else:
    print("El dato no se encuentra en la lista")
