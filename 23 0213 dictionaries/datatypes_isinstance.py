
ages = [21, "23", "sixteen", 26.2, "32.5"]

# active
for age in ages:
    # check if the item is as expected
    if not isinstance(age, (int, float)):
        continue
    remaining = 60 - float(age)
    print(f"{age}, years before turing 60 = {remaining}")