# Problem:  Write a Python program that will ask the user for a letter (alphabet)
#           and will determine whether it is a vowel or a consonant.

letter = input("Enter a letter: ").strip().lower()

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

if letter in vowels:
    print(f"{letter} is a vowel.")
elif letter in consonants:
    print(f"{letter} is a consonant.")
else:
    print(f"{letter} is not a vowel or a consonant.")