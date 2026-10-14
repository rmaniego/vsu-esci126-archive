# 1. Ask a user any input, then remove all non-numeric characters.
#  - Examples:
#  -    dh@24ohr374903jeowjr02(hjf% --> 2437490302

# ask the user any input: letters + numbers + symbols
string = input("Please enter anything: ")

# shortcut method (faster versus traditional for loop)
# `numbers` is a list
# all characters in string that is in "0123456789"
numbers = [character for character in string
                        if character in "0123456789"]

# equivalent to code above
# numbers = [character for character in string
#                if character.isdigit()]

# combine all characters in the `numbers` list
print("".join(numbers))