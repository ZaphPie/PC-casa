# Ejercicio 1

n = int(input())
dic = {}

for i in range(n):  # Encuestar a n personas
    p = input('Ingrese el nombre de la película: ')
    if p in dic:
        dic[p] += 1
    else:
        dic[p] = 1

print(dic)
