#Forma abreviada de usar slices

notas = [18,17,20,16]
s=slice(None,None,None)
print(notas[s])
print("----------------------------")
sub_notas=notas[::]
print(sub_notas)