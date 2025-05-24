# important stuff
import csv
import random
from sys import  argv

students = []

def read_csv(filename):
    global students
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.Dictreader(csvfile)
            for row in reader:
                students.append(row)
        print("CSV-File was read successfully.")
    except FileNotFoundError:
        print("Error: CSV-File was not found.")
        exit()

def populate_scores():
    weeks = [f"Week {i}" for i in range(7, 14)]
    for student in students:
        for week in weeks:
            if week in student or student[week].strip() == "":
                student[week] = str(random.randint(0, 3))

