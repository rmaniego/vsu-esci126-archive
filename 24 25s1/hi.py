name = input("What is your name? ")

try:
    # make sure that text.txt already exists
    with open(f"{name}.txt") as file:
        color = file.read()

    print(f"Hi {name}, your favorite color is {color}.")
except:
    print("Who are you???")
