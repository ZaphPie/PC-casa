
def numMedio(x,y,z):
    if y<x<z or z<x<y:
        return x
    elif x<y<z or z<y<x :
        return y
    elif x<z<y or y<z<x:
        return z


#----------------------------------------------------
print("Input:")
uno=int(input("Numero 1 : "))
dos=int(input("Numero 2 : "))
tres=int(input("Numero 3 : "))
while uno==dos or dos==tres or uno==tres:
    print("Input:")
    uno=int(input("Numero 1 : "))
    dos=int(input("Numero 2 : "))
    tres=int(input("Numero 3 : ")) 
print("Output:")
print("El dato medio es : ",numMedio(uno,dos,tres))