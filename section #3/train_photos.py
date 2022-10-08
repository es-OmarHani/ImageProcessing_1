import cv2 as cv
import numpy as np
import os

#haar_cascaded that read xml file
haar_cascaded = cv.CascadeClassifier('face_detect_default.xml')

#list for people names (from directories)
people = []
for i in os.listdir('Faces\detection') :
    people.append(i)

print(people)
#make variable that have path of file that have faces as directories 
dir = r'C:\Users\dell\OneDrive\Documents\Visual Studio Code\Python\image_proccesing\Faces\detection' 
print(dir)

#lists that will have names and features of faces
features = []
labels = []

#loop on dir that have some of directories with names
for person in people :
    
    #join path of each directory (named by person) with original dir
    dir_path = os.path.join(dir , person )
    label = people.index(person)


    #loop on each image in directory(1 or 2 or 3 or ......)
    for img in os.listdir(dir_path) :
         img_path = os.path.join(dir_path , img)
         gray = cv.imread(img_path , 0)

         #then must detect faces in images
         faces_detect = haar_cascaded.detectMultiScale(gray ,  1.1 , 3)
         for x,y,w,h in faces_detect :
            img_roi = gray[y:y+h , x:x+w]
            features.append(img_roi)
            labels.append(label)


#convert lists (features , labels)
features = np.array(features , dtype='object')
labels   = np.array(labels)

#recognition what in arrays
face_recognition = cv.face.LBPHFaceRecognizer_create()
face_recognition.train(features , labels)

#save all arrays and yml file
np.save('features.npy' , features)
np.save('labels.npy' , labels)
face_recognition.save('face_recognition.yml')

print('Done-------------------------------')

