from tkinter import *
import random

btnList = [None] * 9
fnameLIst = ["ame.png", "black.png", "blue.png", "cafla.png", "cak.png", "coldb.png", "croissant.png", "white.png", "yellow.png"]
photoList = [None] * 9

random.shuffle(fnameLIst)

i, k = 0, 0
xPos, yPos = 0, 0
num = 0 

window = Tk()
window.geometry("300x300")

for i in range(0, 9) :
    photoList[i] = PhotoImage(file="C:\\python1-1\\python1-1-1\\week9\\images\\" + fnameLIst[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 100
    xPos = 0
    yPos += 100
    
window.mainloop()

