import webbrowser
from tkinter import *

root = Tk( )

root.title('Open Browser')
root.geometry('300x200')

def firefox():
    webbrowser.open('https://web.digitalinnovation.one')

myfirefox = Button(root, text='Open DIO', command=firefox).pack(pady=20)
root.mainloop()