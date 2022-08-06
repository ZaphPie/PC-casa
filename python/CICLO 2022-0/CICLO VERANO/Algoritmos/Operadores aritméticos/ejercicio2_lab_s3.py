#Área de un polígono regular

#Input: longitud de lado(float),número de lados(int)
#Output: Área del polígono(float)

from math import tan, pi

lado = float(input("Lado:"))
n= int(input("Número de lados: "))
area= (n *lado**2)/(4*tan(pi/n))
print("El área del polígono regular es: %10.2f"% (area))