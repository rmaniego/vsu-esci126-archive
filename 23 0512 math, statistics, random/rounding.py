import math

number = float(input("Enter any decimal number: "))

round_off = round(number)
round_up = math.ceil(number)
round_down = math.floor(number)

print(f"Round off: {round_off}")
print(f"Round up: {round_up}")
print(f"Round down: {round_down}")