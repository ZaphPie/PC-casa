#ejercicio3 pc1 patrick

n = int(input("n: "))
m = int(input("m: "))
contador= 0
while n > 0:
    if n % 10 == m:
        contador += 1
    n = n // 10
print(contador)


