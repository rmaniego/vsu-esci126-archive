# ask the user's weight in kilograms,

# then compute and display the equivalent weight in Mars.

weight_on_earth = float(input("enter your weight: ")) 
gravity_on_moon = 1.62
gravity_on_earth = 9.81
weight_on_moon = (weight_on_earth / gravity_on_earth) * gravity_on_moon
print(f"The equivalent weight in Moon is {weight_on_moon:,.1f} kg.")
