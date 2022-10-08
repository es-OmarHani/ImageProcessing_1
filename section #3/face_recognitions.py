import cv2 as cv
import numpy as np
import os
import pyttsx3 as py

engine = py.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',0.9)        # setting up volume level  between 0 and 1

                    
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male



#list for people names (from directories)
people = []
for i in os.listdir('Faces\detection') :
    people.append(i)

#haar_cascaded that read xml file
haar_cascaded = cv.CascadeClassifier('face_detect_default.xml')




#import all files
'''
features = np.load('features.npy')
labels = np.load('labels.npy')
'''
#recognition what in arrays
face_recognition = cv.face.LBPHFaceRecognizer_create()
face_recognition.read('face_recognition.yml')

#give him image 
img = cv.imread(r'C:\Users\dell\OneDrive\Documents\Visual Studio Code\Python\image_proccesing\Faces\cal\ben_afflek\2.jpg')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Person' , gray)


#detect face
faces_detect = haar_cascaded.detectMultiScale(gray ,  1.1 , 3) 

for x,y,w,h in faces_detect :
    faces_roi = gray[y:y+h , x:x+w]

    #recognition label and with confidentiality 
    label , confidentiality = face_recognition.predict(faces_roi)
    print(f"{people[label]} is detected with confidentiality = {confidentiality}")

    cv.putText(img , str(people[label]) , (x,y) , cv.FONT_HERSHEY_SIMPLEX , 1.1 , (0,255,0) , 2)
    cv.rectangle(img ,(x,y) , (x+w , y+h) , (0,255,0) , 2)

engine.say(f'Name is {people[label]} ')
engine.runAndWait()

cv.imshow('Detected', img)
cv.waitKey(0)

