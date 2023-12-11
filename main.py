import cv2
import dlib 
import numpy as np

#capture the frame from my primary camera
cap = cv2.VideoCapture(0)

face_detecter = dlib.get_frontal_face_detector()

#capture frames continuously

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    #convert the image into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detecter(gray)
    i=0
    for face in faces:
        x,y=face.left(),face.top()
        x1,y1=face.right(),face.bottom()
        
        cv2.rectangle(frame,(x,y),(x1,y1),(0,255,0),2)
        i=i+1
        cv2.putText(frame,"FACE num"+ str(i), (x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        
    cv2.imshow('frame',frame)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
cap.release()
cv2.destroyAllWindows()

# https://github.com/We5ter/Scanners-Box wifi hacking..