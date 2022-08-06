#Input: n (int) representa el número de elemntos de la lista:
#Output: suma
from random import randint
def sumar(lista):
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        return lista[0]
    return lista[0] + sumar(lista[1:])


#-----------------------Bloque principal
n = int(input("Numero de elementos de la lista: "))
lista = [randint(1,99) for x in range(n)]
print(lista)
print("La suma es: ", sumar(lista))