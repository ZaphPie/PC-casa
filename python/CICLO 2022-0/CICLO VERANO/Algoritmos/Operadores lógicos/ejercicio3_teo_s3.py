#Input: Número de botellas(int)
#Output: Monto(float)

n = int(input("Número de botellas: "))
monto = (n <=5)*(n*4) + ((n>5)*(5*4) +(n-5)*3)
print("El monto a pagar es: ", monto)
print("El monto a pagar es %f" %(monto))