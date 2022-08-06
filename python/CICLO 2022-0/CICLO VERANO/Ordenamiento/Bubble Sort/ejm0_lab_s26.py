def bubble_sort(lista):
    for tope in range(len(lista)-1, 0, -1):  # cuenta las grandes series de ordenamiento
        for i in range(tope):
            if lista[i] > lista[i+1]:  # si dato es más grande que el siguiente ->intercambia posición
                temp = lista[i]
                lista[i] = lista[i+1]  # i+1 -> es el dato de al lado
                lista[i+1] = temp


lista1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(lista1)
print(lista1)
