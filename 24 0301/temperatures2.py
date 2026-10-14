# NOTE: Implement using a List
# Ask the user five (5) temperature readings
# then display the minimum, maximum, and average temperature.

temperatures = []

temperature = float(input(f"Temperature #1: "))
temperatures.append(temperature)

temperature = float(input(f"Temperature #2: "))
temperatures.append(temperature)

temperature = float(input(f"Temperature #3: "))
temperatures.append(temperature)

temperature = float(input(f"Temperature #4: "))
temperatures.append(temperature)

temperature = float(input(f"Temperature #5: "))
temperatures.append(temperature)

minimum = min(temperatures)
maximum = max(temperatures)
average = sum(temperatures) / len(temperatures)

print(f"\nMin. Temperature: {minimum:.1f}")
print(f"Avg. Temperature: {average:.1f}")
print(f"Max. Temperature: {maximum:.1f}")