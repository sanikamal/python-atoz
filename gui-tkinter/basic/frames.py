# Frames
import tkinter

window = tkinter.Tk()
fTop = tkinter.Frame(window)
fTop.pack()
fBot = tkinter.Frame(window)
fBot.pack(side=tkinter.BOTTOM)
lbl1 = tkinter.Label(fTop, text="Hello")
lbl2 = tkinter.Label(fTop, text="Top")
lbl3 = tkinter.Label(fBot, text="Bottom")
lbl1.pack(side=tkinter.LEFT)
lbl2.pack(side=tkinter.RIGHT)
lbl3.pack()
window.mainloop()
