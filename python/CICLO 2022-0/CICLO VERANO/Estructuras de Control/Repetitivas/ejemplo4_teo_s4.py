#Input: num (int)
#Output: suma (float)

num = int(input("Número de términos: "))
suma = 0
c=1
while c <=num:
    suma = suma + pow(c,5)
    c=c+1
print("La sumatoria de los elementos de la serie es:",suma)