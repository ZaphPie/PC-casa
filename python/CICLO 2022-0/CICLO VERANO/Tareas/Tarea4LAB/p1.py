#diccionarios

n = int(input("Numero de personas: "))
dic = {}
for i in range(n):  # Encuestar a n personas
    p = input('Pelicula favorita: ')
    if p in dic:
        dic[p] += 1
    else:
        dic[p] = 1

print(dic)

