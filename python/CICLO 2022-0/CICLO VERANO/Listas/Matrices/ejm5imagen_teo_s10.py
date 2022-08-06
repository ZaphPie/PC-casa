import numpy as np
import matplotlib.pyplot as plt

matrix = np.zeros([100, 300, 3], dtype=np.uint8)

matrix=np.zeros([100, 300, 3], dtype=np.uint8)
matrix[:,:100] = [255,0,0] #ROJO
matrix[:100,:200] = [255,255,255] #BLANCO
matrix[:,200:]=[255,0,0] #ROJO
plt.imshow(matrix)
#cuando hay coma, corta filas y columnas