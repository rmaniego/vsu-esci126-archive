# 1. Ask the user for a letter (alphabet)
# and will determine whether it is a vowel or a consonant.

# STEPS
# 1. Ask    - What is the problem?
# 2. Find   - Gather any information that may help.
# 3. Think  - Come up with possible solutions.
# 4. Choose - Pick the best solution.
# 5. Do     - Try it and make adjustments as needed.
# 6. Code   - Convert the solution into a code.

# kinahanglan nga data
letter = ""
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

# Ask the user for a letter (alphabet)
letter = input("Enter a letter: ")

if letter in vowels:
    # determine whether it is a vowel
    print(f"{letter} is a vowel.")
elif letter in consonants:
    # determine whether it is a consonant.
    print(f"{letter} is consonant.")
else:
    print(f"{letter} is not a vowel or consonant.")