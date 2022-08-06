#EJERCICIO 1.
"""
longitud = int(input())

if longitud >=380 and longitud <= 427:
    print("violeta")
elif longitud >=428 and longitud <= 476:
    print("azul")
elif longitud >=477 and longitud <= 497:
    print("cian")
elif longitud >=498 and longitud <= 570:
    print("verde")
elif longitud >=571 and longitud <= 581:
    print("amarillo")
elif longitud >=582 and longitud <= 618:
    print("naranja")
elif longitud >=619 and longitud <= 780:
    print("rojo")
else:
    print("No corresponde al espectro visible")


#EJERCICIO 2:

r, c, i, j = 0, 0, None, None


a = input()
r = int(input())
c = int(input())
while r <=3:
    r=int(input())
while c <=3:
    c=int(input())
for i in range(1, r + 1):
    for j in range(1, c + 1):
        if i == 1 or i == r or j == 1 or j == c:
            print(end=a)
        else:
            print(end=" ")

    print(end="\n")


#EJERCICIO 3:
carac = input()
multi = int(input())
filas = int(input())


for num in range(0,multi):
	for i in range(filas+1):
		for j in range(filas-i):
			print(carac, end= "")
		print()

#EJERCICIO 4:
serie =[2, 8, 18, 32, 50, 72, 98]
valor=int(input())
while valor<1 or valor>9:
	valor=int(input())
sumserie= 0
sumserie2=2
sumerie3=10
sumserie4=28
sumserie5=60
sumserie6=110
sumserie7=182
sumserie8=280
if valor ==1:
	sumserie=(sumserie)+(serie[0])
elif valor==2:
	sumserie=(sumserie2)+(serie[1])
elif valor==3:
	sumserie=(sumserie3)+(serie[2])
elif valor==4:
	sumserie=(sumserie4)+(serie[3])
elif valor==5:
	sumserie=(sumserie5)+(serie[4])
elif valor==6:
	sumserie=(sumserie6)+(serie[5])
elif valor==7:
	sumserie=(sumserie7)+(serie[6])
if valor==9:
	sumserie = 570
print ("La suma es",sumserie)
"""