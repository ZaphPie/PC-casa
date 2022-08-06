#PROYECTO LITTLE CAD 2d

color_amarillo='\033[93m' 

def crear_matriz():
    matriz = [[' ']*60 for i in range(40)]
    filas=len(matriz)
    columnas=len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if i==0 or i==filas-1:
                matriz[i][j]='•'+color_amarillo
            elif j==0 or j==columnas-1:
                matriz[i][j]='•'+color_amarillo
            else:
                continue
    return matriz

def mostrar_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento,end=' ')
        print( )
    print( )

def guardar_matriz(matriz):
    pass

def menu():
    print('MENU\n'.center(40, ' '))
    print('1) AGREGAR UNA LINEA')
    print('2) AGREGAR UNA ELIPSE O CIRCULO')
    print('3) AGREGAR UN RECTANGULO O CUADRADO')
    print('4) GRABAR UN DIBUJO')
    print('6) LEER UN DIBUJO')
    print('7) MOSTRAR UN DIBUJO')
    print('0) SALIR DEL PROGRAMA\n')
    list_value=[0,1,2,3,4,5,6,7]
    opc=int(input('INGRESE UNA OPCION: '))
    while opc not in list_value:
        opc=int(input('INGRESE UNA OPCION: '))
    return opc

