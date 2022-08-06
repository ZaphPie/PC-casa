#Input:num (int)>0
#Output: El mayor de una lsita de números enteros

from random import randint
def hallarMayor(lista):
    if len(lista) == 0:
        return None
    if len(lista)==1:
        return lista[0]
    if lista[0]>hallarMayor(lista[1:]):
        return lista[0]
    return hallarMayor(lista[1:])


#------------------------------Bloque principal
num=int(input("Número de elementos que tendrá la lista: "))
lista = []
for i in range(num):
    lista.append(randint(1,99))
print(lista)
print("El mayor es: ",hallarMayor(lista))