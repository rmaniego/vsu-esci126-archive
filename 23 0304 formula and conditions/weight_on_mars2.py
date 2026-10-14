weight_on_earth = 0
weight_on_mars = 0
weight_ratio = 0.38

weight_on_earth = float(input("Input weight on earth (kg): "))

weight_on_mars = weight_on_earth * weight_ratio

print(f"Your weight on Mars is {weight_on_mars:,.2f} kg.")