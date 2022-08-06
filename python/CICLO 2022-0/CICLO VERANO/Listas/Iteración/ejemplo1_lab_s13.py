#Input: frase (str), palabra (str)
#Output: mensaje

frase = input("Frase: ")
palabra = input("Palabra a buscar: ")
lista=frase.split()
if palabra in lista:
    print("Si está")
else:
    print("No está")