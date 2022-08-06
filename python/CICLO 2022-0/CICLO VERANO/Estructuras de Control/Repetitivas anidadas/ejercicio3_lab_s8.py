#EJERCICIO 9 DE LA GUÍA

#---------------------------------------------------------
# Dato de Entrada: limite (float)  limite >100
# Dato de salida: tabla de conversion centigrados y kelvin
#----------------------------------------------------------

limite = float(input("Valor limite : "))
while limite<=100:
   limite = float(input("Valor limite : "))
print("%20s %20s" % ("Centigrados", "Kelvin"))
centigrados = 0
while centigrados <=limite:
   print("%20.3f %20.3f" % (centigrados, centigrados + 273.15))
   centigrados = centigrados + 5
print("Adiós...")

