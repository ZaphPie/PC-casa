"""
Haciendo uso de un diccionario, implemente un algoritmo que permita determinar cuántas veces se reoute cada caracter de un string. Considere que su algoritmo debe considerar cualquier caracter(letras,numeros,simbolos,etc.) excepto espacios en blanco.
"""
#-------------------------------------------------------------------------
#  dato de entrada:  frase (str)
# dato de salida:  frecuencia en que cada caracter aparece en la frase
#                  en el conteo no se toma en cuenta el espacio en blanco
#------------------------
def imprimir(dic):
    print("Frecuencias")
    for elem in dic.keys():
        print("%7s %3d" %(elem,dic[elem]))
    
frase = input("Frase: ")
df = { }
for letra in frase:
    if letra !=" ":
        if letra not in df:
            df[letra]=1
        else:
            df[letra]=df[letra]+1
print(df)
imprimir(df)