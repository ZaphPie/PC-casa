#input: frase(str)
#output: longitud de la frase, imprimir la frase de manera vertical,
# imprimir la frase desde la última posición hacia la primera

frase = input("Frase: ")

cont = 0
for letra in frase:
    cont = cont + 1
print("La longitud de la frase es:  ", cont)
#-----ahora imprimimos la frase de manera vertical
for letra in frase:
    print(letra)
#--- ahora imprimimos la frase desde la última posición hacia la primera
i=len(frase)-1
while i>=0:
    print(frase[i], end="")
    i = i-1
print("--------------------------------------")
input("AHORA CON FOR:")
for i in range(len(frase)-1,-1,-1):
    print(frase[i])