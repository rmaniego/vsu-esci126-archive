# Create a Python Program that will that will ask the user
# for a letter (alphabet) and will determine whether it is
# a vowel or a consonant.

# ask the user for a letter (alphabet)
letter = input("Enter a letter (from the alphabet): ")

vowels = "aAeEiIoOuU"
consonants = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ"

if letter in vowels:
    # determine whether it is a vowel
    print(f"'{letter}' is a vowel.")
elif letter in consonants:
    # determine whether it is a consonant.
    print(f"'{letter}' is a consonant.")
else:
    print("Invalid input.")