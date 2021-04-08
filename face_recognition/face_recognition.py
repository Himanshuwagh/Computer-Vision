import cv2
import face_recognition

import cmake
import numpy as np

img=face_recognition.load_image_file('elon.jpg')
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_test=face_recognition.load_image_file('elon_test.jpg')
# img_test=cv2.cvtColor(img_test,cv2.COLOR_BGR2RGB)

faceloc=face_recognition.face_location(img)[0]
encodeimg=face_recognition.face_encodings(img)[0]
faceloctest=face_recognition.face_location(img_test)[0]
encodetest=face_recognition.face_encodings(img_test)[0]

cv2.rectangle(img,(faceloc[3],
                   faceloc[0]),
              (faceloc[1],
               faceloc[2]),
              (255,0,255),2)

results=face_recognition.compare_faces([encodeimg],encodetest)
faceDis=face_recognition.face_distance([encodeimg],encodetest)

print(results,faceDis)

cv2.putText(img_test,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('IMAGE',img)
cv2.imshow('IMAGE TEST',img_test)
cv2.waitKey(1000000)