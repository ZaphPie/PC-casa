import numpy as np
import matplotlib.pyplot as plt

fils = 255
cols = 255
matrix = np.zeros([fils, cols, 3], dtype=np.uint8)

for i in range(fils):
    for j in range(cols):
        matrix[i, j] = [i, j, 0]
plt.imshow(matrix)
