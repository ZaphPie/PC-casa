import numpy as np
import matplotlib.pyplot as plt

fils = 26
cols = 26
matrix = np.zeros([fils, cols, 3], dtype=np.uint8)

for i in range(fils):
    for j in range(cols):
        if i%5==0 or j %5== 0:
            matrix[i,j] = [255,255,255]
        else:
            matrix[i,j] = [0,0,0]
plt.imshow(matrix)