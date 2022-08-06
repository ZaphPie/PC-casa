#Input: Número (int) numero>1
#Output: Factorial (float)

numero=int(input("Número > 1: "))
while numero <=1:
    numero=int(input("Número > 1:"))
#---- ahora calculamos el factorial
factorial = 1
c=1
while c <=numero:
    factorial = factorial * c
    c = c + 1
print("El factorial es:",factorial)
