import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((10,10,3) , dtype='uint8')
plt.imshow(img)
plt.show()

img [:,:,0] = 0.6*255
plt.imshow(img )
plt.show()
