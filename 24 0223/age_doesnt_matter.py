age = int(input("Enter your age: "))

if age < 0:
    print("Not allowed.")
elif age < 18:
	print("You are still a Minor.")
elif age >= 60:
    print("You are a Senior Citizen.")
else:
    print("You are an Adult.")