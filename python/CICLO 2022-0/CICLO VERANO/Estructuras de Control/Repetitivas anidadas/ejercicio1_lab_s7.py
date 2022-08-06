#Input: num (int) num >=1 y num <=9
#Output: triángulo con números

num = int(input("Número <1-9>: "))
while num < 1 or num > 9:
    num = int(input("Número <1-9>: "))
print("Dato leído",num)
#-----construimos el triángulo
for fila in range(1,num+1,1):
    for con in range(1, fila+1,1):
        print(con, end="") #anula el cambio de linea
    #----hacemos el cambio de linea
    print("")
print("\nAdiós...")