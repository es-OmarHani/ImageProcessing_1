import cv2 as cv
import numpy as np

#Normal image
img = cv.imread('photos\park.jpg')
cv.imshow('Normal' , img)

#blank image
blank = np.zeros(img.shape[:2] , dtype='uint8')


#split image
b , g ,r = cv.split(img)
cv.imshow('Blue' , b)
cv.imshow('Green' , g)
cv.imshow('Red' , r)

#printing out shape of this images
print(f'shape of blue = {b.shape} ')
print(f'shape of green = {g.shape} ')
print(f'shape of red = {r.shape} ')


#merge b , g , r with blank image
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('Blue_2' , blue)
cv.imshow('Green_2' , green)
cv.imshow('Red_2' , red)

#printing out shape of this images
print(f'shape_2 of blue = {blue.shape} ')
print(f'shape_2 of green = {green.shape} ')
print(f'shape_2 of red = {red.shape} ')



cv.waitKey(0)
cv.destroyAllWindows()