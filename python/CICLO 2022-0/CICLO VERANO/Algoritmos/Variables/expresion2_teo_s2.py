#---------------------------------------
#Dato de entrada: radio(float), altura(float)
#Dato de salida: área total(float), volumen(float)
#---------------------------------------
from math import pi

radio = float(input("Radio: "))
altura = float(input("Altura: "))
aTotal= 2*pi*radio**2+2*pi*radio*altura
volumen= pi*radio**2*altura
print()
print("El área total es %10.2f" %(aTotal))
print("El volumen es %10.2f" %(volumen))