from tkinter import *
from PIL import Image, ImageTk
import os

window=Tk()



current_path = os.path.dirname(os.path.realpath(__file__))
bg = Image.open(current_path + "/media/hakke_bkg_clean.png")
#bg.resize((175,100))

img1 = ImageTk.PhotoImage(image=bg)
bg_label = Label(window, image = bg)
bg_label.place(x=0, y=0)

btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)


lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)


txtfld=Entry(window, text="This is Entry Widget", bd=0)
txtfld.place(x=80, y=150)


window.title('Hello Python')
window.geometry("875x500+10+10")


window.mainloop()
