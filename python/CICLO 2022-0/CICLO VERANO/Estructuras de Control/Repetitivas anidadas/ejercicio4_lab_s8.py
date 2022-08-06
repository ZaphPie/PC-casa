#EJERCICIO 7 DE LA GUÍA

#Input: num (int) num>=1 y num <=9
#Output: tablas de multiplicar

num = int(input("Número: "))
while num <1 or num >9:
    num = int(input("Número: "))
#-----ahora construimos las tablas
if num % 2 ==0:
    inicio = 2
else:
    inicio = 1
while inicio<=num:
    for i in range(1, 11, 1):
        print(i, "x",inicio, "=", i*inicio)
        print()
        inicio=inicio+2
    print("Adiós...")