import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
    "./python_100_exercises/recursos/frontalface_default.xml"
)

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    
    if ret:
        img = cv2.resize(frame, (700,700))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 2, 3)
        for (x,y,w,h) in faces:
            center = (int(x + w / 2), int(y + h/2))
            axes = (max(int(w /2), 1), max(int(h /2), 1))  # Se utiliza max para asegurar que no haya semiejes de longitud 0
            cv2.ellipse(img, center, axes, 0, 0, 360, (0, 255, 0), 2)
            
            """cv2.rectangle(  
                img,
                (x,y), (x+w, y+h),
                (0, 255, 0), 2
            )"""
    cv2.imshow('faces detected', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()