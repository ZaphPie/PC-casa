num = int(input("Número: "))
while num<=1:
    num=int(input("Número: "))
print("Divisores\n")
for dvisor in range(1, num):
    if (num%dvisor)==0:
        print(dvisor,end=" ")