# 2. Concrete Volume of Structural Components

# Write a Python program that calculates the concrete volume
# of a selected structural component.
# The program shall allow the user to choose among a
#    rectangular slab,
#   rectangular beam,
#   rectangular column, or
#   cylindrical column.

# Depending on the selected component, the program shall request 
# the necessary dimensions in meters and compute the volume
# using the appropriate formula below.

# Rectangular Slab   = Length * Width * Thickness
# Rectangular Beam   = Length * Width * Height
# Rectangular Column = Length * Width * Height
# Cylindrical Column = 3.1416 * Radius ** 2 * Height

# Display the result in cubic meters.

print("OPTIONS: ")
print(" 1 - Rectangular Slab")
print(" 2 - Rectangular Beam")
print(" 3 - Rectangular Column")
print(" 4 - Cylindrical Column")
component = int(input("Enter the structural component: "))

if component in (1, 2, 3):
    length = float(input("Enter the length of the component (m): "))
    width = float(input("Enter the width of the component (m): "))
    
    if component == 1:
        thickness = float(input("Enter the thickness of the component (m): "))
        volume = length * width * thickness
    else:
        # either 2 or 3
        height = float(input("Enter the height of the component (m): "))
        volume = length * width * height
    
    print(f"The volume is {volume:,.2f} cubic meters")
elif component == 4:
    radius = float(input("Enter the radius of the component (m): "))
    height = float(input("Enter the height of the component (m): "))
    volume = 3.1416 * radius**2 * height
    print(f"The volume is {volume:,.2f} cubic meters")
else:
    print(f"Your choice is not in the options.")