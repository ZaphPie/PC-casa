#Input: frase (str)
#Output: imprimir la frase caracter a caracter separado por " "
#SOLUCION 1:
frase =  input("Frase: ")
for letra in frase:
    print(letra, " ", end="")
print()
input("-----------------------------------------enter")
#SOLUCION 2:
phrase=input("Frase: ")
i = 0
while i<len(phrase):
    print(phrase[i], " ", end="")
    i = i+1
print()
input("-----------------------------------------enter")
#SOLUCION 3:
freis=input("Frase: ")
for i in range(0, len(freis),1):
    print(freis[i], " ", end="")