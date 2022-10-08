import cv2 as cv
import numpy as np

#Normal img
img = cv.imread('photos\cats 2.jpg')
cv.imshow('Normal' , img)

#blank img
blank = np.zeros(img.shape[:2] , dtype='uint8')
cv.imshow('blank' , blank)

#rect and circle
rect = cv.rectangle(blank.copy() ,(30,30),(300,300),255,-1)
circle = cv.circle(blank.copy() , (img.shape[1]//2 , img.shape[0]//2 ) , 100 , 255 ,-1 )

#bitwise_xor 
xor = cv.bitwise_xor(rect,circle)
cv.imshow('xor' , xor)

#masking with circle
mask_1 = cv.bitwise_or(img , img , mask = rect)
mask_2 = cv.bitwise_or(img , img , mask = circle)
mask_3 = cv.bitwise_or(img , img , mask = xor)



cv.imshow('mask_1' , mask_1)
cv.imshow('mask_2' , mask_2)
cv.imshow('mask_3' , mask_3)


cv.waitKey(0)
cv.destroyAllWindows()
