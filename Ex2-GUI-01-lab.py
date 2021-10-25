#Andy Villegas
import tkinter as tk

psqs = tk.Tk()
psqs.geometry('300x300')
psqs.configure(bg="Purple")
psqs.title("Ps & Qs")

label_widget = tk.Label(psqs, text="stay on my Ps and my Qs")
label_widget.pack()
label2_widget = tk.Label(psqs, text="stay on my Qs and my Ps", font='times 16 italic', fg='pink', bg='white' ) #changes the font and color of foreground/background


label2_widget.pack()
psqs.mainloop()