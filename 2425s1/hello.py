name = input("What is your name? ")
color = input("What is your favorite color? ")

with open(f"{name}.txt", "w+") as file:
    file.write(color)
