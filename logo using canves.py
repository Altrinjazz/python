import tkinter
from tkinter import Canvas
from tkinter import *
win=tkinter.Tk()
win.geometry("400x400")
win.title("patten")

frame1=Frame(win, bg='blue', borderwidth=2)
frame1.grid(row=0,column=1, padx=10, pady=10) 

def helloCallBack1():
     canvas1.create_line(105,95,115,85,100,70,40,130,100,190,160,130,130,100)
     canvas1.create_line(95,105,85,115,100,130,160,70,100,10,40,70,70,100)

canvas1 = tkinter.Canvas(frame1, bg="SpringGreen2",height=200,width=200)
canvas1.grid(row=0,column=2,padx=10,pady=10)
C= tkinter.Button(frame1, text ="logo", command = helloCallBack1,padx=10,pady=10)
C.grid(row=0,column=0, padx=10, pady=10)

win.mainloop()
