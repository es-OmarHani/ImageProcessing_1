import cv2 as cv
import numpy as np

#read videos
capture = cv.VideoCapture(0)

#haar_cascade that read xml file
haar_cascade = cv.CascadeClassifier('face_detect_default.xml')




while True :

    isTrue , frame = capture.read()
    cv.imshow('Video_NULL' , frame)

    #detect_faces
    detected_faces = haar_cascade.detectMultiScale(frame ,  1.1 , 15)
    print(detected_faces)
    print(f"Number of faces = {len(detected_faces)}")

    #set rect on faces
    for x,y,w,h in detected_faces :
        faces_rect = cv.rectangle(frame , (x,y) , (x+w,y+h) , (255,255,255) , 1)

    cv.imshow('Video_Detected' , faces_rect)

    if cv.waitKey(1) & 0xFF == ord ('q') :
        break

capture.release()
cv.destroyAllWindows()    
