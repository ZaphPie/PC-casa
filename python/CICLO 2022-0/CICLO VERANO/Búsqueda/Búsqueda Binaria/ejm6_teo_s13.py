from random import randint

#-------bloque principal-----------------
n = int(input("Numero de elementos: "))
lista = []
for elem in range(n):
    lista.append(randint(1,99))
print(lista)
print("\nSe ordena la lista de menor a mayor ")
lista.sort() #----modifica la lista
print(lista)
print("\nSe ordena la lista de mayor a menor ")
lista.sort(reverse=True) #ordena de mayor a menor 
print(lista)
#AHORA USANDO soarted():
input("---------------SEGUNDA SOLUCIÓN--------------")
print("Ordenamos de menor a mayor usando sorted")
nuevaLista = sorted(lista) #devuelve una nueva lista
print(nuevaLista)
print("")
print("Ordenamos de mayor a menor usando sorted")
nuevaLista2 = sorted(lista,reverse=True)
print(nuevaLista2)
