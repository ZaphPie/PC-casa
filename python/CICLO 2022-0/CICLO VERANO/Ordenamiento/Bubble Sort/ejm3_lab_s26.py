#Se tiene una lista de diccionarios con información del sistema planetario y se desea tener la lista ordenada de mayor a menor de acuerdo a la cantidad de dias. Utilice el Bubble sort.

def bubble_sort(lista):


    for tope in range(len(lista)-1, 0, -1):
        for i in range(tope):
            if lista[i]["dia"] < lista[i+1]["dia"]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp


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
bubble_sort(misPlanetas)
imprimiLista(misPlanetas)
