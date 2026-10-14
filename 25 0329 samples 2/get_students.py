import csv
# syntax for opening a CSV file
with open("students.csv", newline="") as file:
    
    students = csv.reader(file, delimiter=",")
    for student in students:
        print(" ❤️ ".join(student))