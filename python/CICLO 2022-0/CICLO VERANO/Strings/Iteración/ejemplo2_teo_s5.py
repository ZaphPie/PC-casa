#Input: frase (str)
#Output: imprime la frase al reves

#El efecto solo se ve al imprimir
frase=input("Frase: ")
pos=len(frase)-1
while pos>=0:
    print(frase[pos], end="")
    pos=pos-1