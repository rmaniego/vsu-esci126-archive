# Problem:  Write a Python program that will ask the user
#           for a diameter (in meters) and will display the
#           volume (4/3·πr³) of the sphere, format into 2 decimal places.

PI = 3.1416

diameter = float(input("Enter the diameter (m): ").strip())

volume = (4/3) * PI* ((diameter/2)**3)

print(f"The volume of the sphere is {volume:,.2f} m³.")