from random import randint
def binary_search(lista, e):
    if len(lista) == 1:
        return lista[0] == e

    middle = len(lista)//2
    if lista[middle] == e:
        return True
    elif e < lista[middle]:
        return binary_search(lista[:middle], e)
    else:
        return binary_search(lista[middle:], e)
#-------bloque principal--------------------------------
n = int(input("Numero de elementos: "))
lista = [ ]
for elem in range(n):
    lista.append(randint(1,99))
print(lista)
print("ordenamos la lista:")
lista.sort()
print(lista)
print()
print("Ahora se busca un dato utilizando Busqueda Binaria: ")
dato = int(input("Dato a Buscar: "))
respuesta = binary_search(lista, dato)
if respuesta:
    print("El dato si esta ")
else:
    print("El dato no esta")
