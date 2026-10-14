# Problem:  Write a Python program that will ask the user's weight in kilograms,
#           then compute and display the equivalent weight in Mars.

EARTH_GRAVITY = 9.807
MARS_GRAVITY = 3.721

weight = float(input("Enter your weight (kg): ").strip())

mass = weight / EARTH_GRAVITY
martian_weight = mass * MARS_GRAVITY

print(f"Your weight on Mars is {martian_weight:,.4f} kilograms.")