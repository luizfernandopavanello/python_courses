from tkinter import *

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)


editMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")


goMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Go", menu=goMenu)

goMenu.add_command(label="Back")
goMenu.add_command(label="Forward")
goMenu.add_command(label="Home")


window.mainloop()