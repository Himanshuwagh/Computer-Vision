import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw=mp.solutions.drawing_utils

ptime=0
ctime=0

while True:
    success,img = cap.read()
    imgRBG = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = hands.process(imgRBG)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handls in results.multi_hand_landmarks:
            for id,lm in enumerate(handls.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w) , int(lm.y*w)
                print(id,cx,cy)
                # if id==0:
                    # cv2.circle(img,(cx,cy),20,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handls,mphands.HAND_CONNECTIONS)

    ctime=time.time()
    fps=1 / (ctime-ptime)
    ptime=ctime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)

    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break