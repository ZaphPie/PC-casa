#---recursividad 
def HallaPalabraMasCorta(lista):
    if len(lista)==0:
        return None
    if len(lista)==1:
        return(lista[0])
    if len(lista[0])<len(HallaPalabraMasCorta(lista[1:])):
        return(lista[0])
    else:
        return HallaPalabraMasCorta(lista[1:])
    
#---------------Bloque principal
frase = input("Frase: ")
lista=frase.split()
pal = HallaPalabraMasCorta(lista);
if pal!=None:
    print("La palabra más corta es: ",pal)
    
else:
    print("La frase está vacía")