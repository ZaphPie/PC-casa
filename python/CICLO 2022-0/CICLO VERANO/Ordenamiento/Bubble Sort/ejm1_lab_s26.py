from random import randint


def bubble_sort(lista):
    for tope in range(len(lista)-1, 0, -1):  # cuenta las grandes series de ordenamiento
        for i in range(tope):
            if lista[i] > lista[i+1]: #si dato es más grande que el siguiente ->intercambia posición
                temp = lista[i]
                lista[i] = lista[i+1] #i+1 -> es el dato de al lado
                lista[i+1] = temp


numero = int(input("Numero de elementos : "))
lista = []
for i in range(numero):
    lista.append(randint(1, 50))
print("Lista generada: ")
print(lista)
print("\nImprimimos nueva lista ordenada de menor a mayor: ")
bubble_sort(lista)
print(lista)
