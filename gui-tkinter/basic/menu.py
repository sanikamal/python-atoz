# Menu

import tkinter as tk


def test():
    print('Test')


window = tk.Tk()
mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

fileMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', command=test)
fileMenu.add_command(label='Save', command=test)
fileMenu.add_separator()
fileMenu.add_command(label='Close', command=test)

editMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo')
editMenu.add_command(label='Redo', command=test)
mainMenu.add_command(label='Help')
window.mainloop()
