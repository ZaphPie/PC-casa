#Input: Dos textos
#Output: Indice Jaccard

texto1 = input("Texto 1: ")
texto2 = input("Texto 2: ")

lista1=texto1.split()
lista2=texto2.split()

listaInterseccion=[]
for i in range(len(lista1)):
   if lista1[i] in lista2 and lista1[i] not in listaInterseccion:
       listaInterseccion.append(lista1[i])

listaUnion=[]
for i in range(len(lista1)):
   listaUnion.append(lista1[i])

for i in range(len(lista2)):
   if lista2[i] not in listaUnion:
       listaUnion.append((lista2[i]))

indiceDeJaccard = len(listaInterseccion)/ len(listaUnion)
print("Indice de Jaccard : ", indiceDeJaccard)
