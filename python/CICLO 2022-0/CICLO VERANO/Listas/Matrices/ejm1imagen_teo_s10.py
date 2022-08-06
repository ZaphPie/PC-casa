import numpy as np
import matplotlib.pyplot as plt

filas=255
cols=255
matrix=np.zeros([filas,cols,3],dtype=np.uint8) #tipo de dato
for i in range(filas):
    for j in range(cols):
        matrix[i,j]=[0,0,255]
plt.imshow(matrix) #va a mostrar la imagen