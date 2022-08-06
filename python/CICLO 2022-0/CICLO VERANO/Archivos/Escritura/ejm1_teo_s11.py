#Input: Cadenas (str)
#Output: Crear un archivo "refranes.txt"
#---------------------------------------
miArchivo = open("./refranes.txt","w")
unRefran = input("Refran <fin para terminar>: ")
while unRefran!= "fin":
    miArchivo.write(unRefran+"\n")
    unRefran = input("Refran <fin para terminar>: ")
miArchivo.close()