"""
Diseñe e implemente un algoritmo que reciba como dato de entrada un texto, y proceda a extraer todas las palabras del texto asociado la cantidad de veces que se repite dicha palabra en el texto.
Use un diccionario para guardar cada palabra diferente y las veces que se repite.
"""
#Input: Frase (str)
#Output: Diccionario -> key:palabras ; value: contador
#---------------------------
def imprimir(dic):
    for elem in dic:
        print("%15s %3d" % (elem,dic[elem]))
#------------------------
frase=input("Frase: ")
frase = frase.lower()
lista = frase.split(" ")
print(lista)
print()
diccionario={}
for palabra in lista:
    if palabra not in diccionario:
        diccionario[palabra]=1
    else:
        diccionario[palabra]+=1
print(diccionario)
imprimir(diccionario)