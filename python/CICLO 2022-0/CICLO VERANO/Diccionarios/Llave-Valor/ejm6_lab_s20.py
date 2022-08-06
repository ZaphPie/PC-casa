"""
Use un diccionario para crear un traductor de números del 1 al 10 al japonés. 
"""
#------------------------------------------------
# Dato de entrada: numero (int)
# Dato de salida : nenJapones (str)
#------------------------------------------------
traductor = {1:"Ichi",
             2:"Ni",
             3:"San",
             4:"Yon",
             5:"Go",
             6:"Roku",
             7:"Nana",
             8:"Hachi",
             9:"Kyu",
             10:"Ju"
             }
numero =int(input("Número: "))
if numero in traductor:
    print("El número en japones es: ",traductor[numero])
else:
    print("El número no lo tenemos en el diccionario")