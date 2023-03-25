import tkinter
from tkinter import Canvas
from tkinter import *
win=tkinter.Tk()
win.geometry("850x670")
win.title("Calculator")

def sum():
   a=int(entry1.get())
   b=int(entry2.get())
   c=a+b
   # insert(index,value)
   entry3.insert(0,c)

def sub():
   a=int(entry1.get())
   b=int(entry2.get())
   c=int(a)-int(b)
   # insert(index,value)
   entry3.insert(1,c)

def multiply():
   a=int(entry1.get())
   b=int(entry2.get())
   c=int(a)*int(b)
   # insert(index,value)
   entry3.insert(2,c)

def divide():
   a=int(entry1.get())
   b=int(entry2.get())
   c=int(a)/int(b)
   # insert(index,value)
   entry3.insert(3,c)
   return
def clearing():
   # delete(0,END)
   #entry1.delete(0,END)
   #entry2.delete(0,END)
   entry3.delete(0,END)

frame1=Frame(win, bg='blue', borderwidth=2)
frame1.grid(row=0,column=1, padx=10, pady=10)

label1=Label(frame1, text="Enter number 1:", padx=20, pady=10)
label1.grid(row=0,column=1, padx=10, pady=10)
label2=Label(frame1, text="Enter number 2:", padx=20, pady=10)
label2.grid(row=1,column=1, padx=10, pady=10)
Label3=Label(frame1, text="Result:", padx=20 ,pady=10)
Label3.grid(row=1,column=3, padx=10, pady=10)


entry1=Entry(frame1, width=30, borderwidth=2)
entry1.grid(row=0,column=2, padx=10, pady=10)
entry2=Entry(frame1, width=30, borderwidth=2)
entry2.grid(row=1,column=2, padx=10, pady=10)
entry3=Entry( frame1,width=30, borderwidth=2)
entry3.grid(row=1,column=4, padx=10, pady=10)

add=Button(frame1, text="Add", padx=20, pady=10, command=sum ,fg="red")
add.grid(row=4,column=1, padx=10, pady=10)
sub1=Button( frame1,text="sub", padx=30, pady=10, command=sub,fg="green")
sub1.grid(row=4,column=2, padx=10, pady=10)
multi=Button(frame1, text="multiply", padx=30, pady=10, command=multiply,fg="blue")
multi.grid(row=4,column=3, padx=10, pady=10)
divide1=Button( frame1,text="divide", padx=30, pady=10, command=divide,fg="skyblue")
divide1.grid(row=4,column=4, padx=10, pady=10)
clear=Button(frame1, text="Clear", padx=20, pady=10, command=clearing,fg="purple")
clear.grid(row=4,column=5, padx=10, pady=10)


frame_2 =Frame(win, bg='red', width=350, height=70)
frame_2.grid(row=3,column=1)


def helloCallBack():
  for i in ((100,10),
            (90,20),(110,20),
            (80,30),(100,30),(120,30)):
     canvas.create_text(i,text="*", anchor='center')
     
canvas = tkinter.Canvas(frame_2, bg="skyblue",height=200,width=200)
canvas.grid(row=0,column=1,padx=10,pady=10)
B = tkinter.Button(frame_2, text ="3", command = helloCallBack,padx=10,pady=10)
B.grid(row=0,column=0, padx=10, pady=10)    
      
def helloCallBack1():
     for i in ((100,10),
               (90,20),(110,20),
               (80,30),(100,30),(120,30),
               (70,40),(90,40),(110,40),(130,40)):
      canvas1.create_text(i,text="*", anchor='nw')
canvas1 = tkinter.Canvas(frame_2, bg="SpringGreen2",height=200,width=200)
canvas1.grid(row=0,column=2,padx=10,pady=10)
C= tkinter.Button(frame_2, text ="4", command = helloCallBack1,padx=10,pady=10)
C.grid(row=0,column=3, padx=10, pady=10)


def helloCallBack2():
     for i in ((100,10),
               (90,20),(110,20),
               (80,30),(100,30),(120,30),
               (70,40),(90,40),(110,40),(130,40),
               (60,50),(80,50),(100,50),(120,50),(140,50)):
      canvas2.create_text(i,text="*", anchor='nw')
canvas2 = tkinter.Canvas(frame_2, bg="SpringGreen2",height=200,width=200)
canvas2.grid(row=1,column=1,padx=10,pady=10)
E = tkinter.Button(frame_2, text ="5", command = helloCallBack2,padx=10,pady=10) 
E.grid(row=1,column=0, padx=10, pady=10)   

def helloCallBack3():
     for i in ((100,10),
               (90,20),(110,20),
               (80,30),(100,30),(120,30),
               (70,40),(90,40),(110,40),(130,40),
               (60,50),(80,50),(100,50),(120,50),(140,50),
               (50,60),(70,60),(90,60),(110,60),(130,60),(150,60),
               (40,70),(60,70),(80,70),(100,70),(120,70),(140,70),(160,70)):
      canvas3.create_text(i,text="*", anchor='nw')
canvas3 = tkinter.Canvas(frame_2, bg="light blue",height=200,width=200)
canvas3.grid(row=1,column=2,padx=10,pady=10)
F = tkinter.Button(frame_2, text ="7", command = helloCallBack3,padx=10,pady=10) 
F.grid(row=1,column=3, padx=10, pady=10)   


def clearing():
    clear(0,END)
    canvas.delete("all")
D = tkinter.Button(frame_2, text ="clear", command =clearing,padx=10,pady=10)
D.grid(row=0,column=4, padx=10, pady=10)

win.mainloop()