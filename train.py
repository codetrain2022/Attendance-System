from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
  def __init__(self,root):
    
    self.root = root
    self.root.title("Attendance Manager")
    self.root.state('zoomed')

    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    self.root.configure(bg="#cbf3f0")

    # screen_width = self.root.winfo_screenwidth()
    # screen_height = self.root.winfo_screenheight()

    background_frame = Frame(self.root,bg="#cbf3f0")
    background_frame.place(x=0,y=0,width=screen_width,height=screen_height)
    
    self.train_classifier()
    self.root.destroy()
    

  def train_classifier(self):
    data_dir=("Data")
    path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

    faces=[]
    ids=[]

    for image in path:
      img=Image.open(image).convert('L') #grey scale convertion
      imageNp=np.array(img,'uint8')
      id=int(os.path.split(image)[1].split('.')[1])

      faces.append(imageNp)
      ids.append(id)
      cv2.imshow("Training",imageNp)
      cv2.waitKey(1)==13
    ids=np.array(ids)

    #======================= training the classifier and storing data =================
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")
    cv2.destroyAllWindows()
    messagebox.showinfo("Result","Training data set completed!",parent = self.root)





if __name__=="__main__":
  root=Tk()
  obj=Train(root)
  root.mainloop()