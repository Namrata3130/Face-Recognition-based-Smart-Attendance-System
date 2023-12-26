import cv2
import os

def generate_dataset():
    face_classifier=cv2.CascadeClassifier("haarcascade_profileface.xml")
    name=input("enter name")
    id=input("enter id:")
    class_dir ="Dataset/"+ name
    os.makedirs(class_dir, exist_ok=True)
    def face_cropped(img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.3,5)
        
        if faces is ():
            return None
        for(x,y,w,h) in faces:
            cropped_face=img[y:y+h,x:x+w]
        return cropped_face
    
    cap=cv2.VideoCapture(0)
    
    img_id=0

    while True:
        ret,frame=cap.read()
        if face_cropped(frame) is not None:
            img_id+=1
            face=cv2.resize(face_cropped(frame),(200,200))
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            file_name =  str(id) + "." + str(img_id) + ".jpg"
            file_name_path=os.path.join(class_dir,file_name)
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        #(50,50) is the origin point from where text is to be written.
        
            cv2.imshow("Cropped face",face)
        if cv2.waitKey(1)==60 or int(img_id)==50:
            break
    cap.release()
    cv2.destroyAllWindows()
    print("Collecting Sample is completed.......")

generate_dataset()