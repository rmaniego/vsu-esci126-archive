
ages = [21, "23", "sixteen", 26.2, "32.5"]

# passive
for age in ages:
    try:
        # try to perform this
        remaining = 60 - float(age)
    except Exception as e:
        # if there is an error
        # will jump execution here
        print(f"Error encountered on {age}: {e}")
        continue
    print(f"{age}, years before turing 60 = {remaining}")