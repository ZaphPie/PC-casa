lab104={"202112345":"Juan Medina",
        "202145677":"Sandra Torres",
        "202134567":"Adrian Condori","202156543":"Alexandra Ugarte",
        "202176765": "Angel Hinostroza","202176898":"Arianna Avellaneda"
        }

print(lab104)
print(lab104["202176898"])
print(lab104["202134567"])
lab104["202134567"]="Adrian Condori Condori"
print(lab104)
print()
#------------para recorrer el diccionario----
for clave in lab104.keys():
    print(clave,lab104[clave])
    
#----modificamos el dato asociado a la clave de Angel Hinostroza
lab104["20216765"]="Angel Manuel Hinostroza"
print(lab104)
lab104["202277777"]="James Bond"
print(lab104)