#Input: frase(str)
#Output: nMay, nMin

frase = input("Ingresa la frase: ")
nMay= 0
nMin= 0
for letra in frase:
    if letra >="A" and letra <= "Z":
        nMay= nMay + 1
    elif letra >="a" and letra <="z":
        nMin = nMin + 1

print("La frase tiene: ")
print("Mayúsculas:",nMay)
print("Minúsculas:", nMin)