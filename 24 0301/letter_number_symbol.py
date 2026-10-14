# that will ask the user for a character
character = input("Enter a single character: ") 

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

if character.lower() in letters:
    # and will determine whether it is a letter,
    print(f"'{character}' is a letter.")
elif character in numbers:
    # and will determine whether it is a number.
    print(f"'{character}' is a number.")
else:
    # and will determine whether it is a symbol.
    print(f"'{character}' is a symbol.")


