#Input: Varias palabras hasta que se digite -1
#Output: lista con: vocales abiertas;vocales cerradas; otros

lva = []
lvc = []
otros = []

palabra = input("Palabra [-1 termina]: ")
while palabra != "-1":
    if palabra[0] in "aeoAeo":
        lva.append(palabra)
    elif palabra[0] in "iuIU":
        lvc.append(palabra)
    else:
        otros.append(palabra)
    palabra = input("Palabra [ -1 termina]: ")
print()
print("Lista con palabras que empiezan con vocal abierta ")
print(lva)
print()
print("Lista con palabras que empiezan con vocal cerrada ")
print(lvc)
print()
print("Lista de otras palabras ")
print(otros)
print()
