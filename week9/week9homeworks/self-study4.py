from tkinter import *
from tkinter import messagebox as msg


def keyEvent(event) :
    
    if event.keycode == 37 :
        outp = "shift + 왼쪽 화살표"
    
    elif event.keycode == 38 :
        outp = "shift + 위쪽 화살표"
    
    elif event.keycode == 39 :
        outp = "shift + 오른쪽 화살표"
    
    elif event.keycode == 40 :
        outp = "shift + 아래쪽 화살표"
        
    msg.showinfo("키보드 이벤트",  outp)
   

window = Tk()

window.bind("<Shift-Up>",keyEvent)
window.bind("<Shift-Down>",keyEvent)
window.bind("<Shift-Left>",keyEvent)
window.bind("<Shift-Right>",keyEvent)

window.mainloop()
