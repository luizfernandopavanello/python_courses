from tkinter import *

#  label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='person.png')

label = Label(window,
              text='Code some Python!',
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo
              )

window.mainloop()