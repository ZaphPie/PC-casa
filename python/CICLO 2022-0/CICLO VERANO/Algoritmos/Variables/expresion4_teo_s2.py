#---------------------------------------
#Dato de entrada: segundos(int)
#Dato de salida: dd,hh,mm,ss(int)
#---------------------------------------

SEG_POR_DIA=86400
SEG_POR_HORA=3600
SEG_POR_MIN=60

segundos= int(input("Segundos: "))
#-----------Se realizan los cálculos
dd= segundos //SEG_POR_DIA
segundos= segundos % SEG_POR_DIA
hh= segundos// SEG_POR_HORA
segundos= segundos % SEG_POR_HORA
mm= segundos //SEG_POR_MIN
ss=segundos % SEG_POR_MIN
#-------------Imprimimos los resultados
print()
print("Equivale a: %d:02%d:%02d:%02d" % (dd,hh,mm,ss))
