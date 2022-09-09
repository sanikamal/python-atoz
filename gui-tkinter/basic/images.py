# images
import tkinter as tk

window = tk.Tk()
img = tk.PhotoImage(file='test.png')
img = img.subsample(10)
temp = tk.Label(window, image=img)
temp.pack()

window.mainloop()
