l1=[1,2,3,4,5,6,7,8,9]

lista2=[]
for elem in l1:
    lista2.append(elem*2)
print(lista2)
#Lista por comprensión
l2 = [elem*2 for elem in l1] 
print(l2)