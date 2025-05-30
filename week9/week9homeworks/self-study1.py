from tkinter import *

window = Tk()

liam = PhotoImage(file="C:\\python1-1\\python1-1-1\\week9\\liam.png")
noel = PhotoImage(file="C:\\python1-1\\python1-1-1\\week9\\Noel1.png")

label1 = Label(window, image=liam)
label2 = Label(window, image=noel)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)

window.mainloop()