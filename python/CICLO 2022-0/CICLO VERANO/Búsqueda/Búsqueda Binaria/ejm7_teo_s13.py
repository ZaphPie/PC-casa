#Ahora ordenamos una lista de diccionarios:


misPlanetas = [
    {"planeta": "Mercurio", "diametro": 4878, "año": 88, "dia": 59},
    {"planeta": "Venus", "diametro": 12104, "año": 225, "dia": 5784},
    {"planeta": "Tierra", "diametro": 12760, "año": 365, "dia": 24},
    {"planeta": "Marte", "diametro": 6787, "año": 687, "dia": 24},
    {"planeta": "Jupiter", "diametro": 139822, "año": 4343, "dia": 10},
    {"planeta": "Saturno", "diametro": 120500, "año": 10767, "dia": 11},
    {"planeta": "Urano", "diametro": 51120, "año": 30660, "dia": 18},
    {"planeta": "Neptuno", "diametro": 49530, "año": 60225, "dia": 19}
]

print(misPlanetas)

listaordenada = sorted(misPlanetas, key=lambda funcion: funcion["planeta"])
print("luego de ordenar")
print(listaordenada)


print("Ahora ordeno por diametro")
lista2 = sorted(misPlanetas, key=lambda funcion: funcion["diametro"])
print(lista2)


#  ---https://j2logo.com/python/ordenar-una-lista-en-python/
