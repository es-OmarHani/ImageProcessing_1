import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#image normal
img = cv.imread('images\lower.jpg')
cv.imshow('Normal' , img )

blank = np.zeros ((1000,1000) , dtype='uint8')
blank[:,500:] = 100
cv.imshow('blank' , blank )

#kernels
kernel_X = np.array([[-1,0,1],
                     [-2,0,2],
                     [-1,0,1]])
kernel_y = kernel_X.T

#detects images
detect_1 = cv.filter2D(blank , -1 , kernel_X) 
detect_2 = cv.filter2D(blank , -1 , kernel_y) 
detect = detect_1 + detect_2

cv.imshow('1' , detect_1 )
cv.imshow('2' , detect_2 )
#show detected edges
cv.imshow('final' , detect )

#using canny
canny = cv.Canny(img , 0 , 0)
cv.imshow('canny' , canny )


cv.waitKey(0)

















cv.waitKey(0)