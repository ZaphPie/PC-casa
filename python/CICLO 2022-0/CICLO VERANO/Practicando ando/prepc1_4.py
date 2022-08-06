#ejercicio 4 pc1 patrick
n = int(input())
t=9
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i):
        print(t, end="")
        t= t-1
        if t == -1:
            t=9
    print()