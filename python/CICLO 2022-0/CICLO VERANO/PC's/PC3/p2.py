#2.
print("1. lista con todos los numeros multiplos de 7 comprendidos entre el 7 y el 100")
lista1 = [x for x in range(7, 101, 7)]
print(lista1)
print("2. lista con todods los numeros de dos digitos que sean a la vez multiplos de 2 y de 3")
lista2 = [x for x in range(10, 101, 1)if x % 3 == 0 and x%2==0]
print(lista2)
print("3. matriz de 6 filas por 3 columnas en donde cada elemento sea la caracter #")
lista3 = [['#']*3 for i in range(6)]
print(lista3)

