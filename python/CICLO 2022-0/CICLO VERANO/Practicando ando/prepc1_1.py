#ejercicio1 pc1 patrick

d1_1= int(input("jugador 1 d1:"))
d1_2= int(input("jugador 1 d2:"))
d2_1= int(input("jugador 2 d1:"))
d2_2= int(input("jugador 2 d2:"))

if d1_1 == d1_2 and d2_1 != d2_2:
    print("GANADOR jugador 1")
elif d1_1!=d1_2 and d2_1==d2_2:
    print("GANADOR jugador 2")
else:
    suma1= d1_1 + d1_2
    suma2= d2_1 + d2_2
    if suma1>suma2:
        print("GANADOR jugador 1")
    elif suma1<suma2:
        print("GANADOR jugador 2")
    else:
        print("EMPATE")