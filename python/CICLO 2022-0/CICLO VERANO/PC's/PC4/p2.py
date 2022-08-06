#Recursividad
def listado(lista,palabra):
    lista=[]
    if lista[0]=="fin": 
        return None
    else:
        lista = [].append(palabra)




#--------bloque principal
print("Input:")
listita=[]
palabra = input("Palabra <con Fin termina > : ")
while palabra != "fin":
    palabra = input("Palabra <con Fin termina > : ")
print("Output:")
ListaLeida=listado(listita,palabra)
print("Lista leida: ",ListaLeida)
