def bubble_sort(lista):


    for tope in range(len(lista)-1, 0, -1):
        for i in range(tope):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp


def bubble_sort2(lista):

    for tope in range(len(lista)-1, 0, -1):
        for i in range(tope):
            if len(lista[i]) > len(lista[i+1]):
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp


def contarVocales(palabra):
    c = 0
    for letra in palabra:
        if letra in "aeiouAEIOU":
            c = c+1
    return c


def bubble_sort3(lista):


    #-- ordena por la cantidad de letras vocales que tiene la palabra
    for tope in range(len(lista)-1, 0, -1):
        for i in range(tope):
            if contarVocales(lista[i]) > contarVocales(lista[i+1]):
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp


#--------------bloque principal
frase = input("Ingrese un frase: ")
lista = frase.split()
print(lista)
print("")
print("1. Ordenamos alfabeticamente las palabras")
bubble_sort(lista)
print(lista)
print("")
print("2. Ordenamos de acuerdo a la longitud de las palabras de menor a mayor")
bubble_sort2(lista)
print(lista)
print("")
print("lista ordenada de menor a mayor de acuerdo a la cantidad de letras vocales que tiene cada palabra")
bubble_sort3(lista)
print(lista)
