#Buscar elementos: in e index.
#Si es que únicamente se necesita verificar la existencia de un valor en una lista, se puede utilizar el operador in.
#Si es que adicionalmente se necesita conocer la posición del elemento buscado en la lista, se puede utilizar index. Retornará la posición del primer elemento. IMPORTANTE: En caso no exista el elemento, index generará una excepción.


#Buscando la letra 'e' en la lista
lista_letras=['a','b','c','d','e','f','g','h','i','j','k']
posicion = -1
if 'e' in lista_letras:
    posicion=lista_letras.index('e')
    print("Está en la posición ",posicion)
else:
    print("No hay el elemento en la lista")
