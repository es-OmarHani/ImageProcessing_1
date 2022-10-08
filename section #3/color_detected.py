import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#read image
img = cv.imread('images\img5.png')

img_rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)


#split images
b , g , r = cv.split(img)

lower_1 = np.array([0,0,50])
upper_1 = np.array([50,50,255])
mask_1 = cv.inRange(img , lower_1 , upper_1)
cv.imshow('mask_1',mask_1)

mask_1_1 = cv.inRange(img , lower_1 , upper_1)


lower_2 = np.array([0,50,0])
upper_2 = np.array([50,255,50])
mask_2 = cv.inRange(img , lower_2 , upper_2)
cv.imshow('mask_2',mask_2)

cv.waitKey(0)