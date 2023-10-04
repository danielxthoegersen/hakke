import customtkinter
import csv
from tkinter import *
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 875 #700
    height = 500 #400

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hakkelademands leksikon")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/media/hakke_bkg_clean.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        def print_text():
            total_score = int(score_entry1.get()) + int(score_entry2.get()) + int(score_entry3.get()) + int(score_entry4.get()) + int(score_entry5.get())
            data_str = [film_entry.get(), score_entry1.get(), score_entry2.get(), score_entry3.get(), score_entry4.get(), score_entry5.get(), total_score]
            total_score_label.configure(text=total_score)
            print("Text entered:", data_str)

            # Open the "database.csv" file in append mode ('a', newline='') to add data to it
            with open("database.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                # Write the new_data list as a new row in the CSV file
                writer.writerow(data_str)

            print("Data added to 'database.csv'.")

        # definer indsæt_knap
        button = customtkinter.CTkButton(self, text="Indsæt", command=print_text, text_color="black", fg_color="white", hover_color="gray")

        # definer score_entries
        score_entry1 = customtkinter.CTkEntry(self, placeholder_text="Score", width=50, text_color="black", fg_color="white")
        score_entry2 = customtkinter.CTkEntry(self, placeholder_text="Score", width=50, text_color="black", fg_color="white")
        score_entry3 = customtkinter.CTkEntry(self, placeholder_text="Score", width=50, text_color="black", fg_color="white")
        score_entry4 = customtkinter.CTkEntry(self, placeholder_text="Score", width=50, text_color="black", fg_color="white")
        score_entry5 = customtkinter.CTkEntry(self, placeholder_text="Score", width=50, text_color="black", fg_color="white")

        # definer film_titel_entry
        film_entry = customtkinter.CTkEntry(self, placeholder_text="Filmtitel", text_color="black", fg_color="white")

        # Definer total score
        total_score_label = customtkinter.CTkLabel(self, state="normal", text="...", width=50, text_color="black", fg_color="white")

        # indsæt filmtitel i vindue
        film_entry.place(relx=0.20, rely=0.7125, anchor=CENTER)


        # indsæt scores i vindue
        score_entry1.place(relx=0.385, rely=0.7125, anchor=CENTER)
        score_entry2.place(relx=0.48, rely=0.7125, anchor=CENTER)
        score_entry3.place(relx=0.57, rely=0.7125, anchor=CENTER)
        score_entry4.place(relx=0.657, rely=0.7125, anchor=CENTER)
        score_entry5.place(relx=0.745, rely=0.7125, anchor=CENTER)

        # Indsæt total score i vindue
        total_score_label.place(relx=0.835, rely=0.7125, anchor=CENTER)

        # Indsæt knap i vindue
        button.place(relx=0.5, rely=0.865, anchor=CENTER)

        


       

if __name__ == "__main__":
    app = App()
    app.mainloop()