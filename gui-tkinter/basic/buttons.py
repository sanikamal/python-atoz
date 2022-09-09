# Buttons & Click Event
import tkinter as tk


def handle_click():
    print('Button Clicked')


window = tk.Tk()
btn = tk.Button(window, bd=20, bg='Purple', fg='White', text='Click Me', padx=50, pady=80, command=handle_click)
# btn.pack()
btn.place(x=50, y=50)
window.mainloop()
