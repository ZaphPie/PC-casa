from random import randint
def busquedaBinaria(lista, dato):
    izq = 0
    der = len(lista)-1
    encontrado = False
    while (izq <= der) and not encontrado:
        medio = (izq + der)//2
        if lista[medio] == dato:
            encontrado = True
        else:
            if dato < lista[medio]:
                der = medio - 1
            else:
                izq = medio + 1
    if encontrado:
        return medio
    else:
        return -1


#----- bloque principal------
n = int(input("Numero de elementos: "))
lista = []
for elem in range(n):
    lista.append(randint(1, 99))
print(lista)
print("Ordenamos la lista")
lista.sort()
print(lista)
print()
print("Ahora se busca un dato utilizando Busqueda Binaria: ")
dato = int(input("Dato a Buscar: "))
posicion = busquedaBinaria(lista, dato)
if posicion != -1:
    print("El dato si esta en la posicion:  ", posicion)
else:
    print("El dato no esta")
