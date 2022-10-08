import cv2  as cv 
import numpy as np

blank = np.zeros((500,500,3) ,  dtype='uint8')
cv.imshow('blank' , blank)



#color background
blank[:] = 0,0,255
cv.imshow('blank' , blank)


#rect in image
rect = cv.rectangle(blank , (0,0) , (250,250) , (0,255,0) , thickness=5)
cv.imshow('rect' , rect)

#draw circle
circle = cv.circle(blank , (250,250) , 50 , (250,250,250) , thickness=4)
cv.imshow('circle' , circle)

#draw a line
line = cv.line(blank , (0,0) , (250,250) , (0,0,0) , thickness=5)
cv.imshow('line' , line)

#put text
text = cv.putText(blank , 'Hello omar !' , (100,250) , cv.FONT_HERSHEY_SIMPLEX , 1.0 , (0,0,0) , 6)
cv.imshow('text' , text)

cv.waitKey(0)