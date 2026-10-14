# Problem:  Write a Python program that will ask the user for a character
#           and will determine whether it is a letter, number, or a symbol.

character = input("Enter a character: ").strip().lower()

numbers = "1234567890"
alphabet = "abcdefghijklmnopqrstuvwxyz"

if character in numbers:
    print(f"{character} is a number.")
elif character in alphabet:
    print(f"{character} is a alphabet.")
else:
    print(f"{character} is a symbol.")