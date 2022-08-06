def merge(lista, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i]["planeta"] < right[j]["planeta"]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        lista[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lista[k] = right[j]
        j += 1
        k += 1


def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(lista, left, right)


def imprimiLista(misPlanetas):
    print("[")
    for item in misPlanetas:
        print(item)
    print("]")
    
#----------bloque principal


misPlanetas = [
    {"planeta": "Mercurio", "diametro": 4878, "anio": 88, "dia": 59},
    {"planeta": "Venus", "diametro": 12104, "anio": 225, "dia": 5784},
    {"planeta": "Tierra", "diametro": 12760, "anio": 365, "dia": 24},
    {"planeta": "Marte", "diametro": 6787, "anio": 687, "dia": 24},
    {"planeta": "Jupiter", "diametro": 139822, "anio": 4343, "dia": 10},
    {"planeta": "Saturno", "diametro": 120500, "anio": 10767, "dia": 11},
    {"planeta": "Urano", "diametro": 51120, "anio": 30660, "dia": 18},
    {"planeta": "Neptuno", "diametro": 49530, "anio": 60225, "dia": 19}
]


imprimiLista(misPlanetas)
print("")
print("ahora se ordena por el nombre del planeta en orden alfabetico")
merge_sort(misPlanetas)
imprimiLista(misPlanetas)
