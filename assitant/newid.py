import cv2
import numpy as np
import os
from PIL import Image
import shutil

class trainnewadmin:
    def __init__(self, dirname):
        self.dirname = dirname

    def takephoto(self):
        while True:
            try:
                os.mkdir(self.dirname)
                break
            except:
                shutil.rmtree(self.dirname)
        self.face_cascade = cv2.CascadeClassifier('haarcacade_fronttalface_default.xml')
        self.face_cascade.load('haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        i=1
        while True:
            ret, self.img = self.cap.read()
            self.gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
            self.faces = self.face_cascade.detectMultiScale(self.gray, 1.3, 5)
            for (x,y,w,h) in self.faces:
                s = "hinh.1."+ str(i) + ".png"
                cv2.rectangle(self.img, (x, y), (x+w, y+h), (255,0,0), 2)
                subimg = self.img[y:y+h,x:x+w]
                cv2.imwrite(os.path.join(self.dirname, s),subimg)
                i+=1
            cv2.imshow('img',self.img)
            if i>30:
                break
            k = cv2.waitKey(30) & 0xff
            if k ==27:
                break
            
        self.cap.release()
        cv2.destroyAllWindows()


    def getImageWithID(self,path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg,"uint8")
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            faces.append(faceNp)
            print(ID)
            IDs.append(ID)
            cv2.imshow("training",faceNp)
            cv2.waitKey(10)
        return IDs, faces
    
    def exportxml(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        Ids, faces = self.getImageWithID(self.dirname)
        print(faces)
        self.recognizer.train(faces, np.array(Ids))
        self.recognizer.save("trainningData1.yml")
        cv2.destroyAllWindows()
# a = trainnewadmin("newdata")
# a.takephoto()
# a.exportxml()
