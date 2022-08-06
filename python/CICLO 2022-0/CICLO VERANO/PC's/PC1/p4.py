nFiguras = int(input("Numero de figuras : "))
caracter = input("Caracter : ")
tamanio = int(input("Tamano de la figura : "))
print("")
contador = 1
while contador <=nFiguras:
    cfilas =1
    while cfilas <=tamanio:
        print(caracter * tamanio)
        cfilas = cfilas +1
    print()
    contador = contador + 1
