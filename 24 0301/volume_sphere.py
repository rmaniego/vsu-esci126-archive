

# that will ask the user for a diameter (in meters)
diameter = float(input("Enter a diameter (m): "))

pi = 3.14

radius = diameter / 2

volume = (4/3)*(pi*radius**3)

print(f"The volume of the sphere is {volume:,.2f} cubic meters.")
    
# and will display the volume (4/3·πr³) of the sphere,
# 	format into 2 decimal places.