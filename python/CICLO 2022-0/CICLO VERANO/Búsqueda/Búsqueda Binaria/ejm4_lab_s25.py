def busquedaBinaria(lista,dato):
    izq=0
    der=len(lista)-1
    encontrado= False
    while (izq<=der) and not encontrado:
        medio = (izq+der)//2
        if lista[medio]['año']==dato:
            encontrado=True
        else:
            if dato < lista[medio]['año']:
                der = medio - 1
            else:
                izq = medio + 1
    if encontrado:
        return medio
    else:
        return -1
    
    
#----bloque principal
peliculas = [
    {"titulo": "Shrek", "año": 2001},
    {"titulo": "El viaje de Chihiro", "año": 2002},
    {"titulo": "Valiente", "año": 2012},
    {"titulo": "Frozen", "año": 2013},
    {"titulo": "Buscando a Nemo", "año": 2003},
    {"titulo": "Toy Story 3", "año": 2010},
    {"titulo": "Rango", "año": 2011},
    {"titulo": "Los Increibles", "año": 2004},
    {"titulo": "Wallace y Gromit", "año": 2005},
    {"titulo": "Happy Feet", "año": 2006},
    {"titulo": "Ratatouille", "año": 2007},
    {"titulo": "Wall-E", "año": 2008},
    {"titulo": "Up", "año": 2009}
]

print(peliculas)
datoaBuscar=int(input("Año de la película: "))
#----Se debe ordenar para poder utilizar la busqueda binaria
nueva =sorted(peliculas, key=lambda funcion:funcion['año'])
print("lista ordenada")
print(nueva)
print("")
posicion=busquedaBinaria(nueva,datoaBuscar)
if posicion!=-1:
    print(nueva[posicion])
else:
    print("No existe!!")