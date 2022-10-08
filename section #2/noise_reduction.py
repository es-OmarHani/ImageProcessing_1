import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#image normal
img = cv.imread('images\noisy-img.jpg')
cv.imshow('Normal' , img )





#kernel
kernel = np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]])

#reduce noise
new_img = cv.filter2D(img , -1 , kernel)
cv.imshow('new_img' , new_img )



cv.waitKey(0)


