"""
Es una estrucutra de datos que nos permite almacenar cualquer tipo de valor.
-> Una lista es mutable. Esto significa que puedo modificar sus entradas.

¿Qué son los índices de corte(slices)?
->Así como existen los objetos de tipo int, str y list también existen los objetos de tipo slice.
->Estos objetos están diseñados para ser usados como índices y cortar secuencias
s = slice(inicio,fin,salto)
inicio: será la posición donde comienza el corte
fin: es la posición donde termina el corte (+1)
salto: indica la cantidad de elementos a avanzar en cada paso
"""
#Ejemplo 1:

#lista = [0,1,2,3,4]
lista = [14, 16, 20, 12, 5]
print(lista)
lista[2]=11
print(lista)
print("el tamaño de la lista es: ", len(lista))

#Ejemplo 2:
print("---------------")
notas = [18,17,20,16]
s = slice(1,3,1)
print(notas[s])
p = slice(0,4,1)
print(notas[p])
c=slice(0,4,2)
print(notas[c])