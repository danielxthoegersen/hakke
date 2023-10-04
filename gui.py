# Importing Libraries
from tkinter import *
import customtkinter

# Setting up the theme of the app
customtkinter.set_appearance_mode("dark")

# Setting up the theme of the components
customtkinter.set_default_color_theme("green")

# create CTk window
root = customtkinter.CTk()

# Setting window width and height
root.geometry("300x400")

# Use CTkButton instead of tkinter Button. 
button = customtkinter.CTkButton(master=root, text="Hello World")

# Showing the button at the center of the window
button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Running the app. 
root.mainloop()