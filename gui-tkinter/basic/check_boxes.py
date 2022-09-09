# Check Boxes
import tkinter as tk


def callback():
    print(check_var.get())


window = tk.Tk()
check_var = tk.IntVar()
chb = tk.Checkbutton(window, text='Option 1', width=50, height=10, variable=check_var, command=callback,onvalue=100,
                     offvalue=-100)
chb.pack()
window.mainloop()
