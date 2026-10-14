import csv
def main():
	student = [
            ["Luna Feliz", 21, "Female", "BSGE-2"],
            ["Weljean San", 28, "Male", "BSME-1"]
            
        ]
	with open("students.csv", "a", newline="") as file:
		students = csv.writer(file, delimiter=",")
		students.writerows(student)
 
if __name__ == "__main__":
	main()