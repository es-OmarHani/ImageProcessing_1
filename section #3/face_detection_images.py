import cv2 as cv
import numpy as np

#read image as gray
gray = cv.imread('photos\group 1.jpg')
cv.imshow('Normal' , gray)

#haar_cascade that read xml file
haar_cascade = cv.CascadeClassifier('detected_smile.xml')

#detect_faces
detected_faces = haar_cascade.detectMultiScale(gray ,  1.1 , 10)
print(detected_faces)
print(f"Number of faces = {len(detected_faces)}")

#set rect on faces
for x,y,w,h in detected_faces :
    faces_rect = cv.rectangle(gray , (x,y) , (x+w,y+h) , (255,255,255) , 1)

cv.imshow('Detected_faces' , faces_rect)    

cv.waitKey(0)