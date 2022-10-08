
import cv2 as cv

img = cv.imread("photos\park.jpg")

cv.imshow("normal" , img)



#convert to grey scale
grey = cv.cvtColor(img  , cv.COLOR_BGR2GRAY)
cv.imshow("grey" , grey)


#convert to blur
blur = cv.GaussianBlur(img , (5,5) , cv.BORDER_DEFAULT)
cv.imshow("blur" , blur)


#convert it to canny
canny = cv.Canny(img , 100 , 175)
cv.imshow("Edge Detected" , canny)


#dilating Edges
dilated = cv.dilate(canny , (3,3) , iterations = 3)
cv.imshow("Dilating" , dilated)

#erode Edges
erode = cv.erode(dilated , (2,2) , iterations=2)
cv.imshow("Erode" , erode)

#resize
resized_image = cv.resize(img , (200,200) , interpolation=cv.INTER_AREA )
cv.imshow("resized" , resized_image)

#cropping
cropped = img[0 : img.shape[1] , img.shape[0]//2 : img.shape[0]]
cv.imshow("cropped" , cropped)

cv.waitKey(0)
