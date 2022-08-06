"""
1. primero separa en mitades
2. segundo vuelve a juntar los elementos, pero en orden
"""
from random import randint
def merge_sort(lista):
    if len(lista)>1:
        mid =len(lista)//2
        left=lista[:mid]
        right=lista[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(lista,left,right) #esta función los suma -> los mezcla
def merge(lista,left,right):
    i=j=k=0
    while i <len(left) and j<len(right):
        if left[i]<right[i]:
            lista[k]=left[i]
            i+=1
        else:
            lista[k]=right[j]
            j+=1
            k+=1
    while i<len(left):
        lista[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        lista[k]=right[j]
        j+=1
        k+=1
        

#----- bloque principal------
n = int(input("Numero de elementos: "))
lista = [randint(1, 99) for elem in range(n)]
print(lista)
print("")
print("Ahora se ordena utilizando el algoritmo de ordenamiento de la merge sort")
merge_sort(lista)
print(lista)
