"""
def DoSomething():
    value = 1
    return value


def #keyword
DoSomething #Function name
() #Parentheses
: #Colon
value = 1 #Assigment statement
return value #Return statement

¿Qué es una función?
Son módulos (bloques) de código que realizan alguna tarea específica.
Las funciones “usualmente” toman datos de entrada para “generar” algún resultado

Input x -> Function f: -> Output f(x)

Definición de funciones:

->Es posible que podamos definir nuestras propias funciones:

def suma(numero1,numero2):
    resultado = numero1 + numero 2
    return resultado

Donde: suma -> es el nombre de la función definida
       numero1 -> es el primer parámetro (entrada) de la función
       numero2 -> es el segundo parámetro(entrada) de la función
       resultado -> es la salida que retorna la función


FUNCIONES 2: 
Alcance de una variable: 
Según el alcance de una variable, se las clasifica en:
Variables locales: la variable que se define en un for, 
como cualquier variable local, su alcance se extiende hasta el final de la función en la cual fue definida.

Variables globales:

El alcance de los parámtetros de una función es toda la función.
#EJEMPLO 2# Por ejemplo: El alcance de la variable sideLenght, es la función cubeVolume.

"""

#EJEMPLO:

from math import sqrt
print("Hola, que tal?")
raiz = sqrt(89)
print(raiz)
print("La raiz cuadrada de 123 es:", sqrt(123))

w= 24 +sqrt(111) + 4
print(w)
sqrt(144) #sería un error de lógica
input("-----------enter-------------------------")
#(FUNCIONES PREDEFINIDAS):
#randint es una función predefinida, y para poder usarla hay que invocarla
from random import randint
dado= randint(1,6)
print("Dado: ",dado)
#-----ahora simulamos el lanzamiento de 10 dados
for cont in range(1,11,1):
    dado = randint(1,6)
    print("Dado número %d  %d"% (cont,dado))
input("-----------------EJEMPLO 2---------------------")
#EJEMPLO 2#
def main():
    print(cubeVolume(10))
def cubeVolume(sideLenght):
    return sideLenght**3
main()