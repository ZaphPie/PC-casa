def busquedaLineal(lista,dato):
    #---retorna el indice si no encuentra y -1 si no lo encuentra
    
    for indice in range(len(lista)):
        if lista[indice]['planeta']==dato:
            return indice
    return -1
#-----bloque principal

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
planeta=input("Ingrese nombre del planeta a buscar: ")
posicion=busquedaLineal(lista,planeta)
if posicion !=1:
    print(lista[posicion])
else:
    print("El planeta no existe en la lista!!")