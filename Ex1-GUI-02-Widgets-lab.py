#Andy Villegas
from tkinter import *

pluto = Tk()
pluto.geometry("300x300")
pluto.title('Baby Pluto')

label_widget = Label(pluto, text="Enter Blue or Red")
label_widget.pack() #asks the user for input

enter_text = Entry(pluto, width=20)
enter_text.pack()

def Click():
    sting = enter_text.get() #gets the users input
    if sting == "blue":
        pluto.config(bg="blue")
    elif sting == "red":
        pluto.config(bg="red")
    elif sting == "":
        pluto.config(bg="whitesmoke") #chooses the background color

button = Button(pluto, text="Enter", command=Click)
button.pack()

pluto.mainloop()