
def bubble_sort(lista):
    for tope in range(len(lista)-1, 0, -1):
        for i in range(tope):
            if lista[i] < lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp


#------Bloque principal-----------


asistentes = {
    1: [43, 39, 23, 52, 21, 48, 31, 26, 55, 32],
    2: [51, 29, 47, 40, 32, 25, 31, 29, 51, 36],
    3: [30, 43, 52, 23, 37, 51, 29, 50, 26, 35],
    4: [36, 44, 49, 22, 44, 49, 55, 48, 52, 51],
    5: [32, 29, 43, 32, 32, 36, 22, 48, 38, 29]
}


print("Antes de ordenar:")
for item in asistentes:
    print(item, ": ", asistentes[item])

print("\n\nDespues de ordenar ")
for item in asistentes:
    lista = asistentes[item]
    bubble_sort(lista)
    asistentes[item] = lista

for item in asistentes:
    print(item, ": ", asistentes[item])
