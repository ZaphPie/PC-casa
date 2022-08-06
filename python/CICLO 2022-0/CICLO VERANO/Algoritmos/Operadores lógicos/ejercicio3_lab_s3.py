#Verificar si es triángulo

#Input: l1, l2, l3 (float)
#Output: Mensaje (string) que indique "Es triángulo" o "No es triángulo"

l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

respuesta = (l1 + l2 > l3) and (l2 + l3 > l1) and (l3 + l1 > l2)
print(respuesta * "Es triángulo" + (not(respuesta)) * "No es triángulo" )