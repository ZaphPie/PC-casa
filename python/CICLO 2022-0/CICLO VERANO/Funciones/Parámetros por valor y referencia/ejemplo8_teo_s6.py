#Input: Segundos (int)
#Output: dd,hh,mm,ss (int)

SEG_POR_DIA = 86400
SEG_POR_HORA = 3600
SEG_POR_MIN = 60

def convertir(segundos):
    d = segundos//SEG_POR_DIA
    segundo = segundos %SEG_POR_DIA
    h = segundos//SEG_POR_HORA
    segundos = segundos%SEG_POR_HORA
    m=segundos//SEG_POR_MIN
    s=segundos%SEG_POR_MIN
    return d,h, m,s
#--------------------------------------
segundos =int(input("Segundos: "))
print()
dd,hh,mm,ss = convertir(segundos)
print("Equivale a: %d:%02d:%02d:%02d" % (dd, hh, mm, ss))