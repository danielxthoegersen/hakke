# Importing Libraries
from tkinter import *
import customtkinter

def print_text():
    total_score = int(score_entry1.get()) + int(score_entry2.get()) + int(score_entry3.get())
    data_str = [film_entry.get(), score_entry1.get(), score_entry2.get(), score_entry3.get(), total_score]
    total_score_label.configure(placeholder_text=total_score)
    print("Text entered:", data_str)

# Setting up the theme of the app
customtkinter.set_appearance_mode("dark")

# Setting up the theme of the components
customtkinter.set_default_color_theme("green")

# create CTk window
root = customtkinter.CTk()

# Setting window width and height
root.geometry("700x400")

# Definer indsæt knap
button = customtkinter.CTkButton(master=root, text="Indsæt", command=print_text)


# Definer filmtitel entry
film_entry = customtkinter.CTkEntry(master=root, placeholder_text="Filmtitel")

# Definer score entries
score_entry1 = customtkinter.CTkEntry(master=root, placeholder_text="Score", width=50)
score_entry2 = customtkinter.CTkEntry(master=root, placeholder_text="Score", width=50)
score_entry3 = customtkinter.CTkEntry(master=root, placeholder_text="Score", width=50)


# Definer total score
total_score_label = customtkinter.CTkEntry(master=root, state="normal", placeholder_text="...", width=50, placeholder_text_color="white")




# indsæt filmtitel i vindue
film_entry.place(relx=0.25, rely=0.65, anchor=CENTER)


# indsæt scores i vindue
score_entry1.place(relx=0.5, rely=0.65, anchor=CENTER)
score_entry2.place(relx=0.625, rely=0.65, anchor=CENTER)
score_entry3.place(relx=0.75, rely=0.65, anchor=CENTER)

# Indsæt total score i vindue
total_score_label.place(relx=0.85, rely=0.65, anchor=CENTER)

# Indsæt knap i vindue
button.place(relx=0.5, rely=0.8, anchor=CENTER)



# Running the app. 
root.mainloop()