from tkinter import *

# button = you click it, then it does stuff

def click():
    print('You clocked the button!')

window = Tk()

button = Button(window,
                text='Click Me',
                command=click,
                font=('Comic Sans', 30),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black')

button.pack()

window.mainloop()

