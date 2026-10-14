name = ""
while not name:
    # .strip() remove all preceeding & trailing spaces
    name = input("Enter your name: ").strip()

print(f"\nHello, {name}!")