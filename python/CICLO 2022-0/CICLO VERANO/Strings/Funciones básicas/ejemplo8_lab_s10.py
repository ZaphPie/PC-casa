#input: adn(str)
#output: ci(str) es la cadena complementaria expresada de manera inversa
#ci = complemento inverso
adn = input("ADN: ")
adn = adn.upper()
ci= ""
for i in range(len(adn)-1,-1,-1):
    if adn[i]=="A":
        ci = ci + "T"
    if adn[i]=="T":
        ci = ci+"A"
    if adn[i]=="G":
        ci =ci +"C"
    if adn[i]=="C":
        ci = ci +"G"
print("Cadena inicial: ",adn)
print("Cadena replicada: ",ci)
