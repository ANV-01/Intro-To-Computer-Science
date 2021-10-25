#Andy Villegas
from tkinter import *

ow = Tk()
ow.title('"Vulcanized"')

def button1():
    label1.configure(text="Button One ")
    reset_button.configure(bg="red")

def button2():
    label1.configure(text="Button Two ")
    reset_button.configure(bg="red")

def button3():
    label1.configure(text="Button Three ")
    reset_button.configure(bg="red")

def button4():
    label1.configure(text="Button Four ")
    reset_button.configure(bg="red")

def reset_button():
    label1.configure(text="Reset")
    reset_button.configure(bg="green") #Makes each button have their own assigned color

label1 = Label(ow, text=" ")
label1.grid(row=0, column=1, columnspan=2)

button1 = Button(text="ONE", height=5, width=15, command=button1)
button1.grid(row=1, column=0)

button2 = Button(text="TWO", fg="black", height=5, width=15, command=button2)
button2.grid(row=1, column=1)

button3 = Button(text="THREE", fg="black", height=5, width=15, command=button3)
button3.grid(row=2, column=0)

button4 = Button(text="FOUR", fg="black", height=5, width=15, command=button4)
button4.grid(row=2, column=1) #Makes 4 big buttons that can change the color of the reset button

reset_button = Button(text="Reset", height=10, width=20, bg="yellow", command=reset_button)
reset_button.grid(row=1, column=3, rowspan=2, )

ow.mainloop()