# NOTE: Implement using a List
# Ask the user five (5) temperature readings
# then display the minimum, maximum, and average temperature.

temperatures = []

for count in range(1, 101):
    temperature = float(input(f"Temperature #{count}: "))
    temperatures.append(temperature)

minimum = min(temperatures)
maximum = max(temperatures)
average = sum(temperatures) / len(temperatures)

print(f"\nMin. Temperature: {minimum:.1f}")
print(f"Avg. Temperature: {average:.1f}")
print(f"Max. Temperature: {maximum:.1f}")