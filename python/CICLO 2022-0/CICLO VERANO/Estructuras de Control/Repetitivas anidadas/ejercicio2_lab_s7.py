"""
-Realice un programa que lea un número cuyo rango de valores este entre 1 y 9 y el programa
-Imprima un triángulo como se muestra en el ejemplo:
-ej si num = 9

987654321
98765432
9876543
987654
98765
9876
987
98
9
"""
#Input: num (int) num >=1y num <=9
#Output: triángulo con números

num = int(input("Número: "))
while num<1 or num >9:
    num = int(input("Número: "))

for nf in range(1,num+1,1):
    for cn in range(9,nf-1,-1):
        print(cn, end="")
    print("")

