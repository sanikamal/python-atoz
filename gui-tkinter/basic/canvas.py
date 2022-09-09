# Canvas and Line
import tkinter as tk

window = tk.Tk()
c = tk.Canvas(window, width=300, height=200)
c.pack()
c.create_line(0, 0, 300, 200, fill='Green')
c.create_line(0, 200, 300, 0, fill='Purple')
# create rectangle
c.create_rectangle(100, 20, 200, 120, fill='Green')
c.create_rectangle(120, 40, 180, 140, fill='Yellow')
# create oval
c.create_oval(100, 20, 150, 120, fill='Pink')
window.mainloop()
