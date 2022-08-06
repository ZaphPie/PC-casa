#Copiar una lista:
#Haciendo uso de slicing([:])

lista_numeros=[1,2,3,4,5,6,7,8,9,10]
lista_copia=lista_numeros[:]
print(lista_copia)
lista_numeros[2]=22
lista_numeros[4]=44
print(lista_copia)

#Haciendo uso de la función copy
print("--------------------------------")
lista_numeros=[1,2,3,4,5,6,7,8,9,10]
lista_copia=lista_numeros.copy()
print(lista_copia)
lista_numeros[2]=22
lista_numeros[4]=44
print(lista_copia)