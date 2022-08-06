#DEFINICIÓN-> Una expresión es una combinación de valores, variables, operadores y llamadas funciones.

#---------------------------------------
#Dato de entrada: ancho(float), largo(float)
#Dato de salida: área(float)
#---------------------------------------

ancho = float(input("Ancho: "))
largo =  float(input("Largo: "))
area = ancho*largo
print("El area de la habitación es: %12.4f"% (area))

"""
Especificaciones de formato
%d int
%f float
%s string