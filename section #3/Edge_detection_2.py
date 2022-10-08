import numpy as np 
import cv2 as cv

#read image 
gray = cv.imread('photos\park.jpg')
cv.imshow('Grey' , gray)

#laplacian detect
lab = cv.Laplacian(gray ,cv.CV_64F)
lab = np.uint8(np.absolute(lab))
cv.imshow('Lab' , lab)


#sobel
sobel_x = cv.Sobel(gray ,cv.CV_64F , 1 , 0)
sobel_y = cv.Sobel(gray ,cv.CV_64F , 0 , 1)

cv.imshow('sobel_x' , sobel_x)
cv.imshow('sobel_y' , sobel_y)

combined_sobel_1 = cv.bitwise_or(sobel_x , sobel_y)
cv.imshow('combined_1' , combined_sobel_1)

combined_sobel_2 = sobel_x + sobel_y
cv.imshow('combined_2' , combined_sobel_2)

#canny
canny = cv.Canny(gray , 100 , 0)
cv.imshow('canny', canny)




cv.waitKey(0)


