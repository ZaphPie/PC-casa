entrada=int(input("input: "))
ca=1
conta1=1
conta2=1
conta3=1
dic = {"Aguilas":conta1,"Tigres":conta2,"Halcones":conta3}
while ca<=entrada:
    a=input()
    ca+=1
    if a==dic.keys():
        dic.values(conta1+1,conta2+1,conta3+1)
print(dic)