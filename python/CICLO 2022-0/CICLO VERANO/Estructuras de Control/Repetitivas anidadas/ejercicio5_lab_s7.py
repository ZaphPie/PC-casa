#input: num (int) num>0
#output: triángulo invertido con *

num = int(input("Número < num>0: "))
while num<1:
    num = int(input("Número<num0>: "))
for cf in range(num, -num,-1):
    print("*"* cf)
print("Adiós...")
