#Input: Número Entero (int)
#Output: Lista generada, pero con el valor mayor el inicio
#-------------------------------------
from random import randint

def armarLista(lista):
    elMayor = None
    for nota in lista:
        if elMayor==None or nota>elMayor:
            elMayor = nota
    l2 = [elMayor]
    for i in range(0, len(lista),1):
        if lista [i]!=elMayor:
            l2.append((lista[i]))
    return l2

#---------------------------------
lista = []
ne = int(input("Número de notas: "))
cont = 1
while cont<=ne:
    nota = randint(0,20)
    if nota not in lista:
        lista.append(nota)
    cont +=1
print("Lista: ", lista)
nuevaLista= armarLista(lista)
print("Nueva Lista: ",nuevaLista)