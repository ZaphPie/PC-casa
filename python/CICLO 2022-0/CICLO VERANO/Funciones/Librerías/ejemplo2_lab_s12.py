#------------------------------------------------------------
#-- Dato de Entrada: l1, l2, l3 (int)
#-- Dato de salida:  si es triangulo, tipo de triangulo, area
#------------------------------------------------------------

from modulotriangulo import veSiesTriangulo, veTipodeTriangulo, areaDelTriangulo

l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

esTriangulo = veSiesTriangulo(l1,l2,l3)
if esTriangulo :
   tipodeTriangulo = veTipodeTriangulo(l1,l2,l3)
   print("Es un triangulo : ", tipodeTriangulo)
   print("Su area es      : ", areaDelTriangulo(l1,l2,l3))
else:
   print("No es un triangulo!")
