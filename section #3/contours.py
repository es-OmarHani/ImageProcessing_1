import cv2 as cv
import numpy as np

#read image
img = cv.imread("photos\lady.jpg")
cv.imshow("cats" , img)


#blank image
blank = np.zeros(img.shape , dtype = 'uint8')
cv.imshow('blank' , blank)


#blur image
blur = cv.GaussianBlur(img , (5,5) , cv.BORDER_DEFAULT)


#canny image
canny = cv.Canny(blur , 125 , 175)
cv.imshow('canny' , canny)


#gray scale
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('grey' , grey)


#thresh image
ret , thresh = cv.threshold(grey , 125 , 255 , cv.THRESH_BINARY)
cv.imshow('thresh' , thresh)
 

#read  & drew contours on tresh
contours_1 , hierarchy = cv.findContours(thresh, cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
draw_1 = cv.drawContours(img , contours_1 , -1 , (250,250,250)  , 3) 
draw_1_1 = cv.drawContours(blank , contours_1 , -1 , (250,250,250)  , 3)
cv.imshow('contour_1' , draw_1)
cv.imshow('contour_1_1' , draw_1_1)
print(f"{len(contours_1)} has found in 1")


#read  & drew contours on canny
contours_2 , hierarchy = cv.findContours(canny, cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
draw_2 = cv.drawContours(blank , contours_2 , -1 , (250,250,250)  , 3)
cv.imshow('contour_2' , draw_2)
print(f"{len(contours_2)} has found in 2")




'''
#read  & drew contours on canny
contours_2 , hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL , cv.CHAIN_APPROX_SIMPLE)
draw_2 = cv.drawContours(blank , contours_2 , -1 , (250,250,250)  , 3)
cv.imshow('contour_2' , draw_2)


#read  & drew contours on canny
contours_3 , hierarchy = cv.findContours(thresh, cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
draw_3 = cv.drawContours(blank , contours_3 , -1 , (250,250,250) , 3)
cv.imshow('contour_3' , draw_3)



#importing the module cv2
import cv2
#reading the image whose shape is to be detected using imread() function
imageread = cv2.imread('C:/Users/admin/Desktop/Images/triangle.png')
#converting the input image to grayscale image using cvtColor() function
imagegray = cv2.cvtColor(imageread, cv2.COLOR_BGR2GRAY)
#using threshold() function to convert the grayscale image to binary image
_, imagethreshold = cv2.threshold(imagegray, 245, 255, cv2.THRESH_BINARY_INV)
#finding the contours in the given image using findContours() function
imagecontours, _ = cv2.findContours(imagethreshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#for each of the contours detected, the shape of the contours is approximated using approxPolyDP() function and the contours are drawn in the image using drawContours() function
for count in imagecontours:
epsilon = 0.01 * cv2.arcLength(count, True)
approximations = cv2.approxPolyDP(count, epsilon, True)
cv2.drawContours(imageread, [approximations], 0, (0), 3)
#the name of the detected shapes are written on the image
i, j = approximations[0][0] 
if len(approximations) == 3:
cv2.putText(imageread, "Triangle", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
elif len(approximations) == 4:
cv2.putText(imageread, "Rectangle", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
elif len(approximations) == 5:
cv2.putText(imageread, "Pentagon", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
elif 6 < len(approximations) < 15:
cv2.putText(imageread, "Ellipse", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
else:
cv2.putText(imageread, "Circle", (i, j), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
#displaying the resulting image as the output on the screen
cv2.imshow("Resulting_image", imageread)
cv2.waitKey(0)

'''


cv.waitKey(0)

