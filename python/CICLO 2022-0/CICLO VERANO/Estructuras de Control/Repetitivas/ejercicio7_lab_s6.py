#Input: No tiene
#Output: Números pero respetando las condiciones


"""
SOLUCIÓN 1 - WHILE:
contador = 1
while contador<=1000:
    if contador % 4== contador %6 ==0:
        print(contador,"TicTac")
    elif contador %4 == 0:
        print(contador,"Tic")
    elif contador %6==0:
        print(contador,"Tac")
    else:
        print(contador)
    contador = contador + 1
print("Adiós...")
"""
#SOLUCIÓN 2 - FOR:
for contador in range(1,1001,1):
    if contador %4== 0 and contador %6==0:
        print(contador,"TicTac")
    elif contador % 4==0:
        print(contador,"Tic")
    elif contador % 6==0:
        print(contador,"Tac")
    else:
        print(contador)
print("Adiós...")
