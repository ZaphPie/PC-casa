import imageio
import numpy as np


def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta
    de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen.
    Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3
    dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato bmp.
    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))


class Solution:

    def aplicar_escala_de_rojos(self, lista_3d=leer_imagen('foto_utec.bmp')):
        """
        # Tonos rojos
        # [250, 50, 100]
        # prom = 133
        # [133, 0, 0]
        """
        result = lista_3d
        # SU SOLUCION EMPIEZA AQUI
        for i in result:  # [255,45,125],[48,15,49],[48,35,94]
            for colores in i:  # [255,45,125]  [R,G,B] [SR,SG,SB]
                rojo = colores[0]
                verde = colores[1]
                azul = colores[2]
                a = round((rojo + verde + azul)/3)
                colores[0] = a
                colores[1] = 0
                colores[2] = 0
        # SU SOLUCION TERMINA AQUI
        return result


guardar_imagen("foto_utec_redscale.png", Solution().aplicar_escala_de_rojos())
