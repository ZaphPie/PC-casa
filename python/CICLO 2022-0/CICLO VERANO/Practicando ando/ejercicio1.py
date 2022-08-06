palabra = input("Input: ").lower()
output = {}
for i, char in enumerate(palabra):
    if char not in output.keys():
        output.update({char:[i]})
    else:
        output[char].append(i)
for key,value in output.items():
    print(f"{key}:{value}")
    
