import cv2
import shutil,os
import tkinter as tk
from tkinter import *
global check
def take_photo():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            global name1
            name1=str(name.get())
            img_name = name1+".jpg"
            cv2.imwrite(img_name, frame)
            label()
            break
            #print("{} written!".format(img_name))

    cam.release()

    cv2.destroyAllWindows()


def take_path():
    shutil.copy("source", "destination")

check=0
en=tk.Tk()
en.title("ENROLMENT")
en.geometry("500x500")
l2 = tk.Label(text='ENTER NAME', font='calibre 13 bold', fg='red')
l2.place(x=127, y=105, anchor=CENTER)
name= tk.Entry(bg='white', fg='red', font='calibre 13 bold')
name.place(x=350, y=105, anchor=CENTER, width=300)
b1 = tk.Button(text='Take Photo', font='bold', command=lambda: take_photo(), fg='red')
b1.place(x=150, y=140)

l3 = tk.Label(text='PRESS SPACE BAR TO CAPTURE PHOTO', font='calibre 13 bold', fg='red')
l3.place(x=200, y=200, anchor=CENTER)
def label():
    l3 = tk.Label(text=name1+".jeg sucessfully saved !!", font='calibre 13 bold', fg='red')
    l3.place(x=200, y=200, anchor=CENTER,width=350)
en.mainloop()

