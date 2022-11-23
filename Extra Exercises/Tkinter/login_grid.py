import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()


window_width = 350
window_height = 250


# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# finnd the center poinnt
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)


# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)


root.title('Tkinter Window Demo')


# username
uername_label = ttk.Label(root, text="Username:")
uername_label.grid(column=0, row=0, stick=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, stick=tk.E, padx=5, pady=5)


# password
password_label = ttk.Label(root, text='Password:')
password_label.grid(column=0, row=1, stick=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root, show='*')
password_entry.grid(column=1, row=1, stick=tk.E, padx=5, pady=5)



# login button
login_button = ttk.Button(root, text='Login')
login_button.grid(column=1, row=3, stick=tk.E, padx=5, pady=5)




root.mainloop()
