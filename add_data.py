import csv


film_titel = "Terminator 2"
score_1 = 4
score_2 = 5
score_3 = 7
total_score = score_1 + score_2 + score_3

# Data to be added to the CSV file (replace with your data)
new_data = [film_titel, score_1, score_2, score_3, total_score]

# Open the "database.csv" file in append mode ('a', newline='') to add data to it
with open("database.csv", mode='a', newline='') as file:
    writer = csv.writer(file)
    # Write the new_data list as a new row in the CSV file
    writer.writerow(new_data)

print("Data added to 'database.csv'.")