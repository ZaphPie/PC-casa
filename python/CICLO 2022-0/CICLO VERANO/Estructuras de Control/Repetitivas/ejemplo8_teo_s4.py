#Input: frase (str)
#Output: frase de manera vertical, nMayus, nMinus

frase = input("Frase: ")
nMayus = 0
nMinus = 0
for caracter in frase:
    print(caracter)
    if caracter >="A" and caracter <="Z":
        nMayus = nMayus + 1
    elif caracter >="a" and caracter <="z":
        nMinus = nMinus + 1
print("\nResultados")
print("Número de letras mayúsculas:", nMayus)
print("Número de letras minúsculas:", nMinus)