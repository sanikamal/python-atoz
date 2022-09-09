# Grid

import tkinter as tk

window = tk.Tk()
lblUser = tk.Label(window, text='Username:')
lblPass = tk.Label(window, text='Pass:')
eUser = tk.Entry(window)
ePass = tk.Entry(window)
lblUser.grid(row=0, column=0)
lblPass.grid(row=1, column=0, sticky=tk.E)
eUser.grid(row=0, column=1)
ePass.grid(row=1, column=1)
window.mainloop()
