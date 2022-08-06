def busquedaLineal(lista, dato):
    #-- retorna el indice si no encuentra y -1 si no lo encuentra
    for indice in range(len(lista)):
        if lista[indice] == dato:
            return indice
    return -1


#------- bloque principal-----
listadeNombres = []
nombre = input("Nombre, con fin termina: ")
while nombre != "fin":
    listadeNombres.append(nombre)
    nombre = input("Nombre, con fin termina: ")
print(listadeNombres)
nombreaBuscar = input("Nombre a buscar: ")
posicion = busquedaLineal(listadeNombres, nombreaBuscar)
if posicion != -1:
    print("El nombre esta en la posicion : ", posicion)
else:
    print("El dato no esta en la lista")
