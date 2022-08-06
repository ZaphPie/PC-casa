#Input: num(int)
#Output: mensaje(str)

num=int(input("Número: "))

if num == 0:
    print("El número es cero!")
elif num %2!= 0:
    print("El número es impar!")
else:
    print("El número es par!")
print("Adiós...")