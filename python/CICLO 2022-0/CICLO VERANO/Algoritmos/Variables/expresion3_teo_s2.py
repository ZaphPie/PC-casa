#---------------------------------------
#Dato de entrada: numero(int)
#Dato de salida:suma(int)
#---------------------------------------

numero = int(input("Numero de 3 cifras: "))
unidades = numero % 10
decenas = numero // 10 % 10
centenas = numero// 100
suma = unidades+ decenas + centenas
print()
print("La suma de los dígitos es ", suma)