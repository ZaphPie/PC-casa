#Input: base (int), expo (int)>0
#Output: potencia
def potencia(base,expo):
    if expo==0:
        return 1
    return base *potencia(base,expo-1)




#-------------------------------
base = int(input("Base: "))
expo= int(input("Exponete: "))
while expo <1:
    expo=int(input("Exponete: "))
print("La potencia es: ",potencia(base,expo))