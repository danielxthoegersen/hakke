import os
import csv


# ---------------- Tjek efter database eller opret en ny --------------------- #

# Check if the "database.csv" file exists in the current directory
if os.path.isfile("database.csv"):
    print("The 'database.csv' file already exists.")
else:
    # If it doesn't exist, create an empty CSV file
    with open("database.csv", mode='w', newline=''):
        pass  # This will create an empty file without writing any data
    
    print("Created a new empty 'database.csv' file.")

# Now, you can open and work with the "database.csv" file as needed
with open("database.csv", mode='r') as file:
    reader = csv.reader(file)
    # Your code to read and manipulate the CSV data goes here

# ----------------------------------------------------------------------------- #
