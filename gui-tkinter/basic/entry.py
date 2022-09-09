# Take input from Users(Entry)
import tkinter as tk


def print_value():
    print(userEntry.get())


window = tk.Tk()
userEntry = tk.StringVar()
userEntry.trace('w', lambda name, index, mode: print_value())
e = tk.Entry(fg='Purple', bd=5, bg='White', textvariable=userEntry)
e.pack()
window.mainloop()
