try:
	num = int(input("Enter a number: "))
except ValueError as e:
	print("Value must be an integer.")