# ask the user's weight in kilograms,

# then compute and display the equivalent weight in Mars.

weight_on_earth = float(input("enter your weight: ")) 
gravity_on_mars = 3.71
gravity_on_earth = 9.81
weight_on_mars = (weight_on_earth / gravity_on_earth) * gravity_on_mars
print(f"The equivalent weight in Mars is {weight_on_mars:,.1f} in kilograms.")
