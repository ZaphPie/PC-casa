#ejercicio2 pc1 patrick
"""
n = int(input("n: "))
m = int(input("m: "))
suma = 0
r = 0
for i in range(n):
    r= r*10+m
    suma+=r
print(suma)
"""
n = int(input("n: "))
m = input("m: ")
suma = 0
r = 0
for i in range(1,n+1):
    suma+=int(m*i)
print(suma)
 