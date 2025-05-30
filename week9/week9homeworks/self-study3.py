from tkinter import *
from time import *

fnameList = ["ame.png", "black.png", "blue.png", "cafla.png", "cak.png", "coldb.png", "croissant.png", "white.png", "yellow.png"]
photoList = [None] * 9
num = 0

def clickNext() :
    global num 
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file="C:\\python1-1\\python1-1-1\\week9\\images\\" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    fileName.configure(text=fnameList[num])

def clickPrev() :
    global num 
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file="C:\\python1-1\\python1-1-1\\week9\\images\\" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    fileName.configure(text=fnameList[num])
    

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

photo = PhotoImage(file="C:\\python1-1\\python1-1-1\\week9\\images\\" + fnameList[num])
pLabel = Label(window, image=photo)

fileName = Label(window, text=fnameList[num])

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=300, y=150)
fileName.place(x=325, y=10)
window.mainloop()