import customtkinter
import csv
from tkinter import *
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 875
    height = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hakkelademands leksikon")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/media/hakke_bkg.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

        def print_text():
            film_title = film_entry.get()
            try:
                score1 = int(score_entry1.get())
            except ValueError:
                score1 = 0

            try:
                score2 = int(score_entry2.get())
            except ValueError:
                score2 = 0

            try:
                score3 = int(score_entry3.get())
            except ValueError:
                score3 = 0

            try:
                score4 = int(score_entry4.get())
            except ValueError:
                score4 = 0

            try:
                score5 = int(score_entry5.get())
            except ValueError:
                score5 = 0

            total_score = score1 + score2 + score3 + score4 + score5
            data_str = [film_title, str(score1), str(score2), str(score3), str(score4), str(score5), str(total_score)]
            total_score_label.configure(text=total_score, text_color="black")
            print("Text entered:", data_str)

            # Open the "database.csv" file in append mode ('a', newline='') to add data to it
            with open("database.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                # Write the data_str list as a new row in the CSV file
                writer.writerow(data_str)

            print("Data added to 'database.csv'.")

        def beregn_total(event=None):
            try:
                score1 = int(score_entry1.get())
            except ValueError:
                score1 = 0

            try:
                score2 = int(score_entry2.get())
            except ValueError:
                score2 = 0

            try:
                score3 = int(score_entry3.get())
            except ValueError:
                score3 = 0

            try:
                score4 = int(score_entry4.get())
            except ValueError:
                score4 = 0

            try:
                score5 = int(score_entry5.get())
            except ValueError:
                score5 = 0

            total_score = score1 + score2 + score3 + score4 + score5
            total_score_label.configure(text=total_score, text_color="black")

        button = customtkinter.CTkButton(self, text="HAK!", command=print_text, text_color="black", fg_color="white", hover_color="gray", bg_color="white", border_width=0, width=185)

        score_entry1 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")
        score_entry2 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")
        score_entry3 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")
        score_entry4 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")
        score_entry5 = customtkinter.CTkEntry(self, placeholder_text="...", width=40, text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")

        film_entry = customtkinter.CTkEntry(self, placeholder_text="...", text_color="black", fg_color="white", bg_color="white", border_width=0, justify="center")

        total_score_label = customtkinter.CTkLabel(self, state="normal", text="???", width=40, text_color="gray", fg_color="white")

        film_entry.place(relx=0.21, rely=0.7125, anchor=CENTER)
        score_entry1.place(relx=0.387, rely=0.7125, anchor=CENTER)
        score_entry2.place(relx=0.478, rely=0.7125, anchor=CENTER)
        score_entry3.place(relx=0.57, rely=0.7125, anchor=CENTER)
        score_entry4.place(relx=0.657, rely=0.7125, anchor=CENTER)
        score_entry5.place(relx=0.743, rely=0.7125, anchor=CENTER)
        total_score_label.place(relx=0.834, rely=0.712, anchor=CENTER)
        button.place(relx=0.5, rely=0.865, anchor=CENTER)

        # Bind the beregn_total function to each of the score entry widgets when they lose focus (focus out event)
        score_entry1.bind("<FocusOut>", beregn_total)
        score_entry2.bind("<FocusOut>", beregn_total)
        score_entry3.bind("<FocusOut>", beregn_total)
        score_entry4.bind("<FocusOut>", beregn_total)
        score_entry5.bind("<FocusOut>", beregn_total)

if __name__ == "__main__":
    app = App()
    app.mainloop()
