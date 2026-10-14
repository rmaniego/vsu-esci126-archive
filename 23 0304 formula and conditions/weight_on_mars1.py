weight_on_earth = 0
weight_on_mars = 0

gravity_on_earth = 9.807
gravity_on_mars = 3.721

weight_on_earth = float(input("Input weight on earth (kg): "))

# long-hand-method
# mass = weight_on_earth / gravity_on_earth
# weight_on_mars = mass * gravity_on_mars

weight_on_mars = (weight_on_earth / gravity_on_earth) * gravity_on_mars

print(f"Your weight on Mars is {weight_on_mars:,.2f} kg.")