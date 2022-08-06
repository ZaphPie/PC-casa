#Búsqueda
def busquedaBinaria(lista,dato):
    izq = 0
    der = len(lista)-1
    encontrado = False
    while(izq <= der) and not encontrado:
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
#-----Bloque principal
lista = [
    {"planeta": "Mercurio", "diametro": 4878, "anio": 88, "dia": 59},
    {"planeta": "Venus", "diametro": 12104, "anio": 225, "dia": 5784},
    {"planeta": "Tierra", "diametro": 12760, "anio": 365, "dia": 24},
    {"planeta": "Marte", "diametro": 6787, "anio": 687, "dia": 24},
    {"planeta": "Jupiter", "diametro": 139822, "anio": 4343, "dia": 10},
    {"planeta": "Saturno", "diametro": 120500, "anio": 10767, "dia": 11},
    {"planeta": "Urano", "diametro": 51120, "anio": 30660, "dia": 18},
    {"planeta": "Neptuno", "diametro": 49530, "anio": 60225, "dia": 19}
]

listaordenada = sorted(lista, key=lambda funcion: funcion["planeta"])
planet=input("Planeta: ")
pos = busquedaBinaria(listaordenada,planet)
print("")
if pos != -1:
    print("Diametro : ",listaordenada[pos]["diametro"])
    print("Anio : ",listaordenada[pos]["anio"])
    print("Dia : ",listaordenada[pos]["dia"])
else:
    print("El planeta no existe !")