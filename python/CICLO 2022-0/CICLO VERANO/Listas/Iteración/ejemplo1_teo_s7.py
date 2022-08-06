lista = [12,14,15,16,11,8,9,20,16,14]
print(lista)
suma = 0
contador = 0
for nota in lista:
    suma += nota
promedio = suma/len(lista)
print("El promedio es: ",promedio)

input("--------------2-------------------")
lista = [12,14,15,16,11,8,9,20,16,14]
print(lista)
suma=sum(lista)
cantidad = len(lista)
avg = suma/cantidad
print("El promedio es: ",avg)
