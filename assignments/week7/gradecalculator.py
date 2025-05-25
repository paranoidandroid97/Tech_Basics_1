# important stuff
import csv
import random
import os

students = []

# === STEP 1: Define the CSV path directly ===
# Update this with your actual absolute path to the file
filename = "/Users/phillip/PyCharmMiscProject/assignments/week7/Technical Basics I_2025 - Sheet1.csv"

def read_csv(filepath):
    global students
    try:
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(row)
        print("CSV-File was read successfully.")
    except FileNotFoundError:
        print("Error: CSV-File was not found.")
        exit()

def populate_scores():
    weeks = [f"Week {i}" for i in range(7, 14)]  # Week 7 to 13
    for student in students:
        for week in weeks:
            # Only populate if week is not already filled
            if week in student and student[week].strip() == "":
                student[week] = str(random.randint(0, 3))

def calculate_total(scores):
    best_ten = sorted(scores, reverse=True)[:10]
    return sum(best_ten)

def calculate_average(scores):
    if scores:
        return round(sum(scores) / len(scores), 2)
    else:
        return 0

def calculate_all():
    weeks = [f"Week {i}" for i in range(1, 14) if i != 6]
    for student in students:
        scores = []
        for week in weeks:
            try:
                score = int(student[week])
                scores.append(score)
            except (ValueError, KeyError):
                continue
        student["Total Points"] = calculate_total(scores)
        student["Average Points"] = calculate_average(scores)

def write_csv(filepath):
    if not students:
        print("No student data to write.")
        return

    headers = list(students[0].keys())

    with open(filepath, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

# === MAIN EXECUTION ===
if __name__ == "__main__":
    print("File is being opened:", filename)
    read_csv(filename)
    populate_scores()
    calculate_all()

    user_name = "phillip"  # Use your own name here

    newname = filename.split(".csv")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname)
    print("New file written:", newname)
