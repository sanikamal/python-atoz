# Combo Boxes
import tkinter as tk
import tkinter.ttk as ttk


def callback(event):
    print(event.widget.get())


window = tk.Tk()
tValues = ["A", "B", "C"]
cbx = ttk.Combobox(window, values=tValues)
cbx.set('B')
cbx.bind('<<ComboboxSelected>>', callback)
cbx.pack()
window.mainloop()
