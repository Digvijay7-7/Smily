#Importing Packges
import datetime
import cv2
from tkinter import *
import tkinter.messagebox
import time
import os


root=Tk()
root.geometry('1010x620') 
root.resizable(False,False)
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Smily Cam')
frame.config(background='light blue')
text = Label(frame, text="Smily",bg='light blue',font=('Times 35 bold')) 
text.pack(side=TOP)
filename = PhotoImage(file="img.gif")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)

def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributor","\nDigvijay Patil \n")

def anotherWin(): 
   tkinter.messagebox.showinfo("About",'\n An application to automatically capture selfies when you smile by detecting the smiles \n \n Technology Used \n-OpenCV\n-Tkinter\n ')
                                    
menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)

def exitt():
   exit() 

def detect():
   vid = cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
   smile_cascade = cv2.CascadeClassifier('cascade/haarcascade_smile.xml')

   while True:
         _, frame = vid.read()
         frame1 =cv2.flip(frame,1)
         ori_frame = frame1.copy()
         gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
         face = face_cascade.detectMultiScale(gray, 1.3, 5)
         for x, y, w, h in face:
            cv2.rectangle(frame1, (x,y),(x+w, y+h), (0.255,255),2)
            face_roi = frame1[y:y+h, x:x+w]
            gray_roi = gray[y:y+h, x:x+w]
            smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
            for x1, y1, w1, h1 in smile:
                  cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                  save_img()
         cv2.imshow('Cam Start',frame1)
         if cv2.waitKey(10) == ord('q'):
            destroy()
            break
            
         def save_img():
            folder_path = "Images"
            if not os.path.exists(folder_path):
               os.makedirs(folder_path)
            
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f'selfie-{time_stamp}.png'
            cv2.imwrite(os.path.join(folder_path, file_name), ori_frame)      
            
         def destroy():
            vid.release()
            cv2.destroyAllWindows()

         
but1=Button(frame,padx=4,pady=4,width=25,bg='white',fg='black',relief=GROOVE,command=detect,text='Open Cam & Detect',font=('helvetica 15 bold'))
# but1.place(x=5,y=250)
but1.place(x=680,y=350)

but2=Button(frame,padx=2,pady=2,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
# but2.place(x=210,y=478)
but2.place(x=800,y=450)

root.mainloop()

