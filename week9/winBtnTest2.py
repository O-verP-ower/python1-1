from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("설명", "Liam Gallagher, 1996")


window = Tk()


photo = PhotoImage(file="C:\\python1-1\\python1-1-1\\week9\\liam.png")
button1 = Button(window, image=photo, command=myFunc)

button1.pack()

window.mainloop()