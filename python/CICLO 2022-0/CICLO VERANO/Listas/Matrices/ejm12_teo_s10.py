import numpy as np
import  matplotlib.pyplot as plt
from PIL import Image
image = Image.open("macchupicchu.jpg")
matrix=np.array(image)
plt.imshow(matrix[:400])