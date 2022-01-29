from tkinter import *

def pressKey(event):
    # print('You pressed: ' + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind('<Key>', pressKey)

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()

