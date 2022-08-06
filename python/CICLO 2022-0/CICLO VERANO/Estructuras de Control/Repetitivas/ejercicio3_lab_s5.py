#Input: num(int)
#Output: Tabla de multiplicar desde 1 al 10 de num

num = int(input("Número: "))
cont = 1
while cont <= 10:
    print(cont,"x",num,"=", cont*num)
    cont = cont + 1
print("Adiós...")