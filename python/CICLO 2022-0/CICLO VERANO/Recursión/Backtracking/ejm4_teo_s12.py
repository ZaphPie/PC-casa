# Input: Divisor, dividendo (int)
#Output: Cociente (int)

def cociente(d, dsor):
    if d < dsor:
        return 0
    return 1 + cociente(d - dsor, dsor)


# Bloque principal-----------------------------------
dividendo = int(input("Dividendo : "))
while dividendo <= 0:
    dividendo = int(input("Dividendo : "))
divisor = int(input("Divisor: "))
while divisor <= 0:
    divisor = int(input("Divisor: "))
print("El cociente es: ",  cociente(dividendo, divisor))
