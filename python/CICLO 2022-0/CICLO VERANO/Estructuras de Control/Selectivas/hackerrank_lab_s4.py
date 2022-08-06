#EJERCICIO 1:
n1 = int(input())
n2 = int(input())
suma = n1 + n2
print("La suma es",suma)
input("-------------------------")

#EJERCICIO 2:
pi=3.1415
n=float(input())
rpta=(n*180)/pi
rpta=round(rpta,3)
print("Grados Sexagesimales",rpta)
input("-------------------------")

#EJERCICIO 3:
colores=int(input())
c24=colores//24
colores=colores%24
c12=colores//12
colores= colores%12
c6=colores//6
colores=colores%6

print("C24",c24)
print("C12",c12)
print("C6",c6)
print("Sobran",colores)

#EJERCICIO 4:
x=int(input())
y=int(input())
z=int(input())

a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print(a,b,c)

#EJERCICIO 5:
def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum
n=int(input())
if getSum(n)%2==0:
    print("La suma de los digitos es par")
else:
    print("La suma de los digitos es impar")
