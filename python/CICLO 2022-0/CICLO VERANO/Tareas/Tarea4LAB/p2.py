#recursividad
from random import randint
def sumaImpares(lista,i=0,suma=0):
    if len(lista)==i:
        return suma
    elif lista[i]%2!=0:
        suma+=lista[i]
        return sumaImpares(lista,i+1,suma)
    else:
        return sumaImpares(lista,i+1,suma)

#----bloque principal
n=int(input("Numero : "))
lista=[]
for i in range(n):
    lista.append(randint(1,99))
print(lista)
print("La suma de los numeros impares es : ",sumaImpares(lista))