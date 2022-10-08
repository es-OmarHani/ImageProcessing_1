import cv2 as cv
import numpy as np

img = cv.imread("photos\park.jpg")
cv.imshow('cat' , img)



#retranslation function
def translation(image , x , y) :
    transMatrix = np.float32 ([[1,0,x],[0,1,y]])
    dim = (image.shape[1] , image.shape[0])
    return cv.warpAffine(image , transMatrix , dim)

translated_IMAGE = translation(img , 100 , 100)
cv.imshow("translated" , translated_IMAGE)


#flip image
flipped = cv.flip(img ,0)
cv.imshow("flipped" , flipped)


cv.waitKey(0)


