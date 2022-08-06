"""
from random import randint
i = 10
x = []
cont = 1
while cont <=10000:
  cont+=1
  x.append(randint(1,10000))
a = slice(20, i, -2)
b = slice(500, i*25, -50)
x1 = x[a]
x2 = x[b]
print(x)
print (x1)
print (x2)
"""
"""
num = input()
x = int(num)
f = str(x)*x
print(f)
"""

a = int(input())
b= int(input())
def function(a, b):
    mb = 1
    for i in range(2, b):
        if b % i == 0:
            mb = i

    ma = 1
    for i in range(2, a):
        if b % i == 0:
            ma = i

    if mb == ma or (mb % 3 == 0 and ma % 3 == 0):
        return True
    return False
