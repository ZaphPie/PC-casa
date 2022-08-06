#Input: numeros (int) se ingresan varias numeros, terminar con el CERO
#Output: promedio (float)

suma = 0
contador = 0
numero = int(input("Número: "))
while numero != 0:
    contador = contador + 1
    suma = suma + numero
    numero = int(input("Número:"))
if contador > 0:
    promedio = suma /contador
    print("El promedio es: ", promedio)
else:
    print("No se han ingresado numeros validos")