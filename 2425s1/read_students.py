import csv

# syntax for opening a CSV file
with open("students.csv", newline="") as file:
    students = csv.reader(file, delimiter=",")
    students = list(students)

for student in students:
    print(student[0], end=", ")
