from random import *
#rellenos los datos en aquella matriz
#TOTAL DE MEDALLAS
#LA MAS REPARTIDA
'''
matriz=[[400,350,290],
        [390,320,280],
        [260,330,270],
        [230,300,260],
        [220,310,270]]

filas=5
columnas=3

'''
# MATRIZ FILA COLUMNA
#print(matriz[0][0]+matriz[0][1]+matriz[0][2])
'''

oro=0
plata=0
bronce=0

for i in range(filas):
    #       filas columnas
    oro+=matriz[i][0]
    plata+=matriz[i][1]
    bronce+=matriz[i][2]

lista=[oro,plata,bronce]    
lista_2=['ORO','PLATA','BRONCE']

A=0
for e in lista:
    if e>A:
        A=e

print(A)

mximo=max(lista)
            #lista.index(valor a buscar)
print(oro)
print(plata)
print(bronce)
print(lista_2[lista.index(mximo)])
'''
'''
filas=int(input('INGRESE FILAS'))
columnas=int(input('INGRESE COLUMNAS'))

#1 OPCION
matriz_0=[[0]*columnas for i in range(filas)]

#2 OPCION
matrix=[]
for i in range(filas):
    matrix.append([0]*columnas)
#CAMBIAR VALORES
for i in range(filas):
    for j in range(columnas):
        matrix[i][j]=randint(1,999)


#OPCION 3
matriz_3=[]
for i in range(filas):
    nueva=[]
    for i in range(columnas):
        nueva.append(randint(1,99))
    matriz_3.append(nueva)

print(matriz_0)
print()
print(matrix)
print()
print(matriz_3)
'''
'''
filas=2
columnas=3

matriz=[[24,15,18],[58,47,49]]
matriz_2=[[154,24,15],[48,57,489]]
matriz_3=[]

for i in range(filas):
    nuevo=[]
    for j in range(columnas):
        nuevo.append(matriz[i][j]+matriz_2[i][j])
    matriz_3.append(nuevo)

print(matriz_3)
'''
'''
def suma_diagonal(matriz,filas,columnas):
    suma=0
    for i in range(filas):
        for j in range(columnas):
            if i==j:
                #          fials columnas
                suma+=matriz[i][j]
    
    print(suma)

suma_diagonal([[1,2,3],[3,4,5],[5,6,7]],3,3)
'''
'''
def funcion1(texto):
    a=[e for e in texto if e.isalpha()==False]
    #a=['␣','␣']
    print(texto.split(a[0]))

funcion1('hola␣como␣estas')
'''
'''
def funcion2(matriz,columnas,filas,n):
    mayores=[matriz[i][j] for i in range(filas) for j in range(columnas) if matriz[i][j]>n]
    menor=[matriz[i][j] for i in range(filas) for j in range(columnas) if matriz[i][j]<n]
    print(menor,',',mayores)

funcion2([[1,2,3],[4,5,6],[7,8,9]],3,3,5)
'''
'''
def funcion3(lista1,lista2):
    interseccion=[numero for numero in lista1 if numero in lista2]
    print(interseccion)

funcion3([1,2,3,4,5],[10,4,5,6])
'''
'''
def funcion4(texto):
    diccionario={}
    minuscula=texto.lower()
    #letra por letra
    a=[e for e in minuscula if e.isalpha()==False]#'␣'
    #separas
    separas=minuscula.split(a[0])

    #separs=['hola','mi,'nombre']
    for palabra in separas:
        if palabra in diccionario:
            diccionario[palabra]+=1
        else:
            diccionario[palabra]=1

    print(diccionario)

funcion4('Hola␣mi␣nombre␣es␣Miguel␣y␣el␣nombre␣de␣mi␣gata␣es␣Agatha')
'''
'''
archivo=open('MATRICES\input.txt','r')
lista=[]
for linea in archivo:
    lista.append(linea)

invertir_lista=lista[::-1]

invertir=open('inv.txt','w+')
for line in invertir_lista:
    invertir.write(line[::-1])


#[hola,jose]
#aloh

#[4,5,6]
#[6,5,4]
'''

matriz=[[2,3,4],
    [0,4,10],
    [0,0,1]]

filas=3
columnas=3

si_cumple=0
for i in range(filas): #1
    for j in range(i): #0
        if matriz[i][j]==0:
            si_cumple=1
        else:
            si_cumple=0
            break
si_cumple_2=0
for i in range(filas):
    for j in range(columnas):
        if i==j:
            if matriz[i][j]>=0:
                si_cumple_2=1
            else:
                si_cumple_2=0

if si_cumple==1 and si_cumple_2==1:
    print('LA MATRIZ ES TRIANGULAR SUPERIOR')