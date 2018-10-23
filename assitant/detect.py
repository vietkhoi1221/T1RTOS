import cv2
import numpy as np
import speech
def recog():
    faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("trainningData1.yml")
    id = 0
    i =0
    Id = ""
    # front = cv2.InitFont(cv2.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
    while True:
        ret,img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
            id,conf = rec.predict(gray[y:y+h,x:x+w])
            cv2.putText(img,str(id),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255))
            if(conf<70):
                if(id==1):
                    Id="Khoi" 
                    break      
            else:
                Id="Khong Biet"
            i+=1
        cv2.imshow("Face",img)
        if(i>60):
            i=0
            speech.say("Thằng nào đó")
        if((cv2.waitKey(1) == ord("q"))):
            return False
            break
        if (Id=="Khoi"):
            speech.say("Xác nhận thành công.")
            print("Xác nhận thành công.")
            return True
            cam.release()
            cv2.destroyAllWindows()
            break
        print(Id)
    cam.release()
    cv2.destroyAllWindows()