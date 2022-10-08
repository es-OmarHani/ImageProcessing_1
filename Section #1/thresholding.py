import cv2 as cv
import numpy as np

img = cv.imread('photos\cats.jpg',0)
cv.imshow('Normal' , img)

#normal threshold
threshold , thresh_img_1 =  cv.threshold(img , 150 , 255, cv.THRESH_BINARY )
print(threshold)
cv.imshow('thresh_img_1' , thresh_img_1)


#adaptive threshold 
thresh_img_2 = cv.adaptiveThreshold(img ,255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 , 3)
cv.imshow('thresh_img_main' , thresh_img_2)

#adaptive threshold 
thresh_img_3 = cv.adaptiveThreshold(img ,255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 11 , 3)
cv.imshow('thresh_img_gauss' , thresh_img_3)

cv.waitKey(0)