def busquedaBinaria(lista, dato):
    izq = 0
    der = len(lista)-1
    encontrado = False
    while(izq < der) and not encontrado:
        medio = (izq+der)//2
        if lista[medio]['planeta'] == dato:
            encontrado = True
        else:
            if dato < lista[medio]['planeta']:
                der = medio-1
            else:
                izq = medio+1
    if encontrado:
        return medio
    else:
        return -1


# -----bloque principal
lista = [
    {"planeta": "Mercurio", "diametro": 4878, "año": 88, "dia": 59},
    {"planeta": "Venus", "diametro": 12104, "año": 225, "dia": 5784},
    {"planeta": "Tierra", "diametro": 12760, "año": 365, "dia": 24},
    {"planeta": "Marte", "diametro": 6787, "año": 687, "dia": 24},
    {"planeta": "Jupiter", "diametro": 139822, "año": 4343, "dia": 10},
    {"planeta": "Saturno", "diametro": 120500, "año": 10767, "dia": 11},
    {"planeta": "Urano", "diametro": 51120, "año": 30660, "dia": 18},
    {"planeta": "Neptuno", "diametro": 49530, "año": 60225, "dia": 19}
]

print(lista)
print('')
# ---- se tiene que ordenar los datos de acuerdo al planeta
listaordenada = sorted(lista, key=lambda funcion: funcion['planeta'])
print("Nueva lista ordenada")
print(listaordenada)

planetaaBuscar = input("Ingrese nombre del planeta a buscar: ")
posicion = busquedaBinaria(listaordenada, planetaaBuscar)
if posicion != -1:
    print(listaordenada[posicion])
else:
    print("El planeta", planetaaBuscar, "no existe en la lista")
