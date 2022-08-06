from re import I
from codigo_c import *

def main_general():
    matrixx=crear_matriz()
    look=mostrar_matriz(matrixx)
    value=menu()

    if value==1:
        punto1=(input("INGRESE UNA COORDENADA inicial (x,y): ") ).split(",") #
        punto2=(input("INGRESE UNA COORDENADA final (x,y): ")).split(",") #
        valores1=list(map(int,(punto1)))
        valores2=list(map(int,(punto2)))
        
        for i in range(len(matrixx)-2,-1,-1):
            for j in range(len(matrixx[0])-2):
                if i==j and i<4 or j<4:
                    matrixx[i][j]='X'
                    
                    

    elif value==2:
        pass
    elif value==3:
        pass
    elif value==4:
        pass
    elif value==5:
        pass
    elif value==6:
        pass
    elif value==7:
        pass
    elif value==0:
        print('GRACIAS POR SU TIEMPO')

main_general()
