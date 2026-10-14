import csv
def main():
	# syntax for opening a CSV file
	with open("students.csv", newline="") as file:
		students = csv.reader(file, delimiter=",")
		for student in students:
			print(", ".join(student))

if __name__ == "__main__":
	main()