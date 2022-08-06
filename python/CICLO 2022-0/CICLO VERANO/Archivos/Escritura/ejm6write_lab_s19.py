aFuente = open("./numeritos.txt","r")
aDestino= open("./copia.txt","w")

unDato = aFuente.readline()
while unDato !="":
    aDestino.write(unDato)
    unDato =aFuente.readline()
aFuente.close()
aDestino.close()