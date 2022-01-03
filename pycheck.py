from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

root = Tk()
root['background'] = "#cbf3f0"
student_img = Image.open(r"Assets/1927248-200.png")
student_img_photo = ImageTk.PhotoImage(student_img)
label = Button(root,image=student_img_photo,border=0,bg = "#cbf3f0",fg = "#cbf3f0")
label.pack()


root.mainloop()