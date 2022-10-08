import cv2 as cv

img = cv.imread('photos\cats.jpg')
cv.imshow("Normal" , img)

#blur tec
blur = cv.blur(img , (5,5) )
cv.imshow("blur" , blur)

#gaussian_blur
gauss = cv.GaussianBlur(img , (5,5) , 0)
cv.imshow("gauss" , gauss)

#median_blur
median = cv.medianBlur(img , 5 )
cv.imshow("median" , median)

#bilateral
bilateral = cv.bilateralFilter(img , 5 , 51 , 51)
cv.imshow("bilateral" , bilateral)

cv.waitKey(0)





