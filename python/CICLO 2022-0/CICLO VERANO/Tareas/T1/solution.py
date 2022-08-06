class Solution:
    # RECORDAR RETORNAR LA RESPUESTA

    def palabrasUtecsinas(self, palabra):
        lenght = len(palabra)
        while lenght < 4:
            palabra = str(input(palabra))
        if "u" in palabra and "t" in palabra and "e" in palabra and "c" in palabra:
            return True
        else:
            return False
        
    def rectanguloEspecial(self, longitud, altura, letra_base, letra_especial):

        figura_rectangular = ""
        dpot = abs(longitud-altura)
        for c in range(altura):
            for h in range(longitud):
                if (c + h) % dpot == 0:
                    figura_rectangular += letra_especial
                elif (c + h) % dpot!= 0:
                    figura_rectangular += letra_base
            if c < altura - 1:
                figura_rectangular += "\n"
            else:
                pass
        return figura_rectangular


# === CASOS EJEMPLO ===
print(Solution().palabrasUtecsinas("cuenta"))  # output en consola: True
print(Solution().rectanguloEspecial(6, 4, "O", "L"))
"""
output en consola:      LOLOLO
                        OLOLOL
                        LOLOLO
                        OLOLOL
"""
