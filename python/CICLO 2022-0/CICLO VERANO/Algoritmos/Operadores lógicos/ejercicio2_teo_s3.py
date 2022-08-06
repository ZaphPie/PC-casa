#INPUT: número(int)
#OUTPUT: mensaje(str) "Es par" o "Es impar"


numero = int(input("Número: "))
rpta= numero % 2 ==0
print(rpta*"Es par" + (not(rpta))*"Es impar")