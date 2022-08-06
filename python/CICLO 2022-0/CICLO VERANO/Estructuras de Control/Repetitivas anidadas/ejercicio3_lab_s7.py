#input: num (int) num>0
#output: triángulo con *
"""
num = int(input("Número < num>0: "))
while num<1:
    num = int(input("Número<num0>: "))
for cf in range(1,num+1,1):
    for ca in range(1, cf+1,1):
        print("*",end="")
    print()
"""
num = int(input("Número < num>0: "))
while num<1:
    num = int(input("Número<num0>: "))
for cf in range(1, num+1,1):
    print("*"* cf)
