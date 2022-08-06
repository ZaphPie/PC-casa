#input: frase (str)
#output: numMay,numMin, numVocales (int)

frase = input("Frase: ")

numMay = 0
numMin = 0
numVocal= 0

for i in range(0,len(frase),1):
    if frase[i] >="A" and frase[i] <="Z":
        numMay = numMay + 1
    if frase[i] in "abcdefghijklmnopqrstuvwxyz":
        numMin = numMin + 1
    if frase[i] in "AEIOUaeiou":
        numVocal=numVocal + 1
print("Número de letras mayúsculas: ",numMay)
print("Número de letras minúsculas: ",numMin)
print("Número de letras vocales: ",numVocal)

