num = int(input("Número de elementos: "))
lista = []
for cont in range(1,num+1,1):
    dato= int(input("Dato: "))
    lista.append(dato)
print(lista)
input("------------2------------")
print("Imprimimos los elementos de la lista utilizando while")
i=0
while i<len(lista):
    print(lista[i]," ", end="")
    i+=1
print("Imprimimos los elementos de la lista con el for ")
for elemento in lista:
    print(elemento," ", end="")
print("\nImprimimos los elementos de la lista con el for con rango")
for i in range(0,len(lista),1):
   print(lista[i]," ", end="")