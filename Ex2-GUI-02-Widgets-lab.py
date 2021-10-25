#Andy Villegas
from tkinter import *

ow = Tk()
ow.geometry('300x300')
ow.title('"The Ten"')

box1= BooleanVar()
box2= BooleanVar()
box3= BooleanVar()

def Check():
    if box1.get() == 1:
        label1.configure(text="True")
    elif box1.get() == 0:
        label1.configure(text="False")
    if box2.get() == 1:
        label2.configure(text="True")
    elif box2.get() == 0:
        label2.configure(text="False")
    if box3.get() == 1:
        label3.configure(text="True")
    elif box3.get() == 0:
        label3.configure(text="False")
    temp_var = Var.get()
    L1.configure(text=temp_var)   #Displays True or False on the label(s)

label1 = Label(ow,text=" ")
label2 = Label(ow,text=" ")
label3 = Label(ow,text=" ")

button1 = Button(ow, text="Enter", command=Check)

cb1 = Checkbutton(ow,text="Checkbutton 1",variable=box1)
cb2 = Checkbutton(ow,text="Checkbutton 2",variable=box2)
cb3 = Checkbutton(ow,text="Checkbutton 3",variable=box3)
cb1.select()
cb2.select()
cb3.select() #Diplays the check buttons

Var = IntVar()

L1 = Label(ow,text=" ")

rb1 = Radiobutton(ow)
rb1.configure(text="Radiobutton 1", variable=Var, value=1)
rb2 = Radiobutton(ow)
rb2.configure(text="Radiobutton 2", variable=Var, value=2)
rb3 = Radiobutton(ow)
rb3.configure(text="Radiobutton 1", variable=Var, value=3) #Displays the radio buttons

rb1.pack()
rb2.pack()
rb3.pack()
L1.pack()

cb1.pack()
cb2.pack()
cb3.pack()

label1.pack() #runs the code
label2.pack()
label3.pack()

button1.pack()

ow.mainloop()