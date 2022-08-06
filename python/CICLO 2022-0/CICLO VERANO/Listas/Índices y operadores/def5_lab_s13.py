#Eliminar elementos: del, remove y pop
#Si se necesita eliminar una porción de la lista, se utiliza la función del
lista_letras = ['a','b','c','d','e','f','g','h','i','j','k']
#Eliminar el elemento de la posición 3
del lista_letras[3]
print(lista_letras)
#Eliminar los 2 primeros elementos
del lista_letras[:2]
print(lista_letras)
#Eliminar los elementos desde la posición 2 hasta el 4
del lista_letras[2:6]
print(lista_letras)
#Eliminar la variable lista_letras
del lista_letras

#Si se necesita eliminar la primera ocurrencia de un valor, se utiliza la función remove.

#Eliminar la letra 'g' de la lista
lista_letras = ['a','b','c','d','e','f','g','h','i','j','k']
lista_letras.remove('g')
print(lista_letras)

#Si se necesita eliminar un elemento por su posición en la lista, se puede ulilizar la función pop. Por defecto, pop eliminará el último elemento de la lista y retornará el valor de elemento eliminado.
lista_letras=['a','b','c','d','e','f','g','h','i','j','k']
#Obtiene y elimina el último elemento de la lista
elemento =lista_letras.pop()
print(elemento)
#Obtiene y elimina el tercer y cuarto elemento de la lista
elemento = lista_letras.pop(3)
print(elemento)
elemento=lista_letras.pop(4)
print(elemento)
print(lista_letras)