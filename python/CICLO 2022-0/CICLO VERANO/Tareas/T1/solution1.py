class Solution():
    def espacio(self,x,r):
        #input: Cantidad de pelotas (int) ; Radio de las pelotas (float)
        #Output: Volumen en cm**3 (float)
        pi = 3.1415

        volumen=(4/3)*(pi)*(r**3)
        respuesta = volumen*x  # debe ser un numero decimal
        return respuesta

print(Solution().espacio(5, 2.9))