miArchivo = open("./refranes2.txt","w")
unRefran = input("Refran: ")
while unRefran!="fin":
    miArchivo.write(unRefran + "\n")
    unRefran=input("Refran: ")
miArchivo.close()