
frase = input("Refran: ")
lfrase = frase.split()
vocal = []
cons = []
for i in lfrase:
    if i[len(i)-1].lower() in ["a", "e", "i", "o", "u"]:
        vocal.append(i)
    else:
        cons.append(i)
print("Palabras que terminan en vocal : ",vocal)
print("Palabras que terminan en consonante : ",cons)
