from random import randint


def bubble_sort(lista):
    for tope in range(len(lista)-1, 0, -1):  # cuenta las grandes series de ordenamiento
        for i in range(tope):
            if lista[i] > lista[i+1]:  # si dato es más grande que el siguiente ->intercambia posición
                temp = lista[i]
                lista[i] = lista[i+1]  # i+1 -> es el dato de al lado
                lista[i+1] = temp


#---------bloque principal-------
n = int(input("Numero de elementos: "))
lista = [randint(1,99) for elem in range(n)]
print(lista)
print("")
print("Ahora se ordena utilizando el algoritmo de ordenamiento de la Bubble sort")
bubble_sort(lista)
print(lista)