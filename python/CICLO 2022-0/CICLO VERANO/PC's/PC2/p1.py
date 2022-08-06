print("Input:")
nashe = input("Palabra: ")
nashe = nashe.upper()
cont=0
for char in nashe:
    if char=='A': cont+=1
    elif char=='E':cont+=1
    elif char =='I':cont+=1
    elif char=='O':cont+=1
    elif char=='U':cont+=1
print()
print("Output:")
if cont>=5:
    print("La palabra tiene las 5 vocales!")
else:
    print("La palabra no tiene las 5 vocales!")
