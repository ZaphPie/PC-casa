#input: dia, mes, año (int)
#output: ángel (str)

dia= int(input("Dia: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if año % 2 == 0:
    if mes >=1 and mes <= 3:
        if dia %2==0:
            print("Su ángel es Miguel")
        else:
            print("Su ángel es Gabriel")
    elif mes<= 6:
        if dia % 2==0:
            print("Su ángel es Jofiel")
        else:
            print("Su ángel es Raziel")
    elif mes <= 9:
        if dia%2==0:
            print("Su ángel es Chamuel")
        else:
            print("Su ángel es Zelatiel")
    else:
        if dia %2==0:
            print("Su ángel es Uriel")
        else:
            print("Su ángel es Jeremiel")
else:
    if mes>=1 and mes <=3:
        if dia %2==0:
            print("Su ángel es Rafael")
        else:
            print("Su ángel es Uriel")
    elif mes<=6:
        if dia %2==0:
            print("Su ángel es Barachiel")
        else:
            print("Su ángel es Jehudiel")
    elif mes <=9:
        if dia%2==0:
            print("Su ángel es Zadkiel")
        else:
            print("Su ángel es Metatron")
    else:
        if dia % 2==0:
            print("Su ángel es Anael")
        else: print("Su ángel es Azrael")
