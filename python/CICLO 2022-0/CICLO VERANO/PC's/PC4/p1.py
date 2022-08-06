# Diccionarios
from json import dumps
print("Input: ")
frase = input("Frase: ")
dic = {}

for palabra in frase.split():
    if palabra not in dic.values():
        dic.update({len(palabra): palabra})


print(dumps(dic, indent=4))