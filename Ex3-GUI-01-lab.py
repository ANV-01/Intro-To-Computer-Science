#Andy Villegas
from tkinter import *
import random
ow = Tk()
ow.geometry('300x300')
ow.configure(bg="black")
ow.title('"OFF-WHITE"')#sets up the window for our gui program

label_widget = Label(ow, text='"Label"')
label_widget.pack() #makes a label widget
label2_widget = Label(ow, text='"Label 2"', font='Serif 16 bold', fg='black', bg='white')
label2_widget.pack()

def Click():
 myLabel = Label(ow, text='"Button Pressed"')
 myLabel.pack() #function to call back upon when the button is used

def Click2():
 label_widget.config(text='"Random Number"')
 randnum = random.randint(1, 100)
 label2_widget.config(text = randnum, font = 'Serif 16 bold', fg = 'black', bg = 'white') #changes the first 2 labels made into Random Number and selects a random number from 1-100

button1 = Button(ow, text='"Button 1"', command=Click)
button1.pack()

button2 = Button(ow, text='"Button 2"', command=Click2,font='Serif 16 bold', fg='black', bg='white')
button2.pack() #defines what Button 1/2 will do

ow.mainloop()