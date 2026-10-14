

temperature = [81, 29, 33, 39, 44, 24]

minimum_value = min(temperature)
maximum_value = max(temperature)

print(f"Minimum temperature: {minimum_value} degrees C")
print(f"Maximum temperature: {maximum_value} degrees C")

average = sum(temperature) / len(temperature)

print(f"Average temperature: {average:.2f} degrees C")