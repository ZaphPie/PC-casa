mag = float(input("Magnitud: "))
if mag<2:
    print("El sismo es Micro")
elif 2<=mag<3:
    print("El sismo es Muy Menor")
elif 3<=mag<4:
    print("El sismo es Menor")
elif 4<=mag<5:
    print("El sismo es Ligero")
elif 5<=mag<6:
    print("El sismo es Moderado")
elif 6<=mag<7:
    print("El sismo es Fuerte")
elif 7<=mag<8:
    print("El sismo es Mayor")
elif 8<=mag<10:
    print("El sismo es Cataclismo")
else:
    print("El sismo es Meteórico")