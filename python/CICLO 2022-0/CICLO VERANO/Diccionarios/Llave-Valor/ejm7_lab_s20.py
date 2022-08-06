#--------------------------------------------
#Input: frase(str)
#Output: Frecuencias de las palabras
#--------------------------------------------

def imprimir(d):
    for elemento in d.keys():
        print("%12s %3d" %(elemento,d[elemento]))

frase = input("Frase: ")
frase = frase.lower()
listadepalabras = frase.split()
print(listadepalabras)
dicdeFrecuencias={}
for palabra in listadepalabras:
    if palabra in dicdeFrecuencias:
        dicdeFrecuencias[palabra] +=1
    else:
        dicdeFrecuencias[palabra]=1 ### Estamos insertando un valor al diccionario, una palabra nueva
imprimir(dicdeFrecuencias)