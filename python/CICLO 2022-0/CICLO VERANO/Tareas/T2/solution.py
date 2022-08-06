class Solution():
    def transformacion(self, cadena):
        informacion = []
        CAMBIO = False

        auxiliar = 0
        for i in range(len(cadena)):
            s = ['*', '-', '#']
            if CAMBIO == False:
                if cadena[i] in s:
                    informacion.append(int(cadena[auxiliar:i]))
                    auxiliar = i
                    CAMBIO = True
            else:

                if cadena[auxiliar] == '-' and (cadena[i] == '-' or cadena[i] == '#' or cadena[i] == '*'):
                    informacion.append((cadena[auxiliar+1:i]))
                    auxiliar = i

                elif cadena[auxiliar] == '*' and (cadena[i] == '-' or cadena[i] == '#' or cadena[i] == '*' or cadena[i] == cadena[(len(cadena)-1)]):
                    informacion.append(int(cadena[auxiliar+1:i]))
                    auxiliar = i

                elif cadena[auxiliar] == '-' and cadena[i] == cadena[len(cadena)-1]:
                    informacion.append((cadena[auxiliar+1:i+1]))
                    auxiliar = i
                elif cadena[auxiliar] == '#' and (cadena[i] == '#'):
                    auxiliar = i+1


        return informacion
