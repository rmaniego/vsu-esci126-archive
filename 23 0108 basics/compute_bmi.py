# Problem:  Write a Python program
# that will ask the user's weight in kilograms and height in meters,
# then compute and display the body mass index.

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / (height**2)

print(f"\nYour BMI is {bmi:.2f}.")