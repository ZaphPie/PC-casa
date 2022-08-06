mat=[[2,3,4],
     [40,50,60],
     [100,200,300]
     ]

s = [sum(item)for item in mat]
print(s)

total=sum([elem for item in mat for elem in item])
print(total)