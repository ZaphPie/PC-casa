#-----------------------------
#Input: num(int)
#Output: Lista con valores aleatorios,listaPares,listaImpares
#-----------------------------
from random import randint

num= int(input("Número de elementos: "))
lista = []
for cont in range(1,num+1,1):
    valor = randint(1,100)
    lista.append(valor)
print(lista)
#------ahora formamos dos nuevas listas (pares, impares)
input("--------------------------2--------------------------------")
listadePares=[]
listadeImpares=[]
for i in range(0,len(lista),1):
    if lista[i]%2==0:
        listadePares.append(lista[i])
    else:
        listadeImpares.append(lista[i])
print()
print("Lista de pares: ")
print(listadePares)
print()
print("Lista de impares: ")
print(listadeImpares)