from turtle import color
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#read image
img = cv.imread('photos\cats.jpg')
cv.imshow('Normal' , img)


#blank image
blank = np.zeros(img.shape[:2] , dtype='uint8')
cv.imshow('blank' , blank)


#grey_scale
gray_img = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Grey_scale' , gray_img)

#circle them mask
circle = cv.circle(blank ,(img.shape[1]//2 , img.shape[0]//2) , 100 , (250,250,250) , -1)
mask = cv.bitwise_and(gray_img ,gray_img ,mask=circle)
cv.imshow('Masking' , mask)


#histogram of grey with mask
gray_hist = cv.calcHist([gray_img] , [0] , mask , [256] , [0 , 256])

plt.figure()
plt.title('Grey_Histogram')
plt.xlabel('# of bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist , color='b')
plt.xlim( [0 , 270] ) 
plt.show()


#histogram of image with mask
colors = ('b','g','r')

#plot figure
plt.figure()
plt.title('image_Histogram')
plt.xlabel('# of bins')
plt.ylabel('# of pixels')

for i , color in enumerate(colors) :

    img_hist = cv.calcHist([img] , [i] , mask , [256] , [0 , 256])

    plt.plot(img_hist , color=color)
    plt.xlim( [0 , 270] ) 

plt.show()

