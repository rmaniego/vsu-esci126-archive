# initialize a variable called 'name' with an empty value: ""
name = ""

# while the name is still empty
while not name:
    # ask the user for his/her name
	name = input("Enter your name: ").strip()

print(f"\nHello, {name}!")