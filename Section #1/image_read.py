import cv2 as cv


#read image 
img = cv.imread("photos/cat_large.jpg")

#resize function
def resize_scale (frame , scale) :
    width  = int( frame.shape[1] * scale) 
    height = int( frame.shape[0] * scale) 
    dim = (width , height)
    return cv.resize ( frame , dim , interpolation = cv.INTER_AREA)


#read image resized
img_resize = resize_scale(img , 0.6)
cv.imshow('cat_resize' , img_resize)


#image show normal
cv.imshow('cat' , img)


cv.waitKey(0)