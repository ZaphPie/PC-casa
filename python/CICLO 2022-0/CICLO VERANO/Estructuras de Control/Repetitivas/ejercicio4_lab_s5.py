#Input: 5 notas(float)
#Output: promedio (float)

suma = 0
contador = 1
while contador<= 5:
    nota = float(input("Nota: "))
    suma = suma + nota
    contador = contador + 1
promedio = suma / 5
print("El promedio es: %10.3f"% (promedio))


