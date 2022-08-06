#Área de Triángulo
#Input: L1, L2, L3 (float)
#Output: Área del triángulo (float)
from math import sqrt

l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

#Calcular el semiperímetro(s)
s=(l1+l2+l3)/2
#Calcular el área
area= sqrt(s*(s-l1)*(s-l2)*(s-l3))
print("El área del triángulo es: %12.3f"%(area))