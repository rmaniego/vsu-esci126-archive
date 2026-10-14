# 2. Concrete Slab Volume and Cost Estimation

# Write a Python program that estimates 
# the volume and total cost of concrete required for a rectangular slab.
# The program shall accept the length, width, and thickness 
# of the slab in meters, along with the cost of concrete per cubic meter.
# Compute and display the concrete volume in cubic meters
# and its corresponding total cost using the following formulas:

# Volume = Length * Width * Thickness
# Total Cost = Volume * Cost per Cubic Meter

length = float(input("Enter the length of the slab (meters): "))
width = float(input("Enter the width of the slab (meters): "))
thickness = float(input("Enter the thickness of the slab (meters): "))



volume = length * width * thickness
print(f"The total volume of the slab is {volume:,.2f} cubic meter.")


cost = float(input("Enter the cost of the slab (per cubic meter, in pesos): "))
total_cost = volume * cost

print(f"The total cost is P{total_cost:,.2f}")

#       (length)
#     __________
#    /_________/| --> thickness
#   |_________|/  --> width