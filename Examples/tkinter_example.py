from tkinter import *
from PIL import Image, ImageTk
import os

window=Tk()



current_path = os.path.dirname(os.path.realpath(__file__))
bg = Image.open(current_path + "/media/hakke_bkg.png")
bg = bg.resize([875, 500])

img1 = ImageTk.PhotoImage(image=bg)
bg_label = Label(window, image = img1)
bg_label.place(x=0, y=0)

btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=90, y=100)


lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)


txtfld=Entry(window, text="This is Entry Widget", bd=0, width=20, bg="white", fg="black", highlightcolor="white", highlightthickness=0)
txtfld.place(x=94, y=346)


window.title('Hello Python')
window.geometry("875x500+10+10")


window.mainloop()
