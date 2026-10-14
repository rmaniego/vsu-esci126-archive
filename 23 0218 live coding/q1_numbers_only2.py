# 1. Ask a user any input, then remove all non-numeric characters.
#  - Examples:
#	- dh@24ohr374903jeowjr02(hjf% --> 2437490302

# initialize an empty list (gi-ready lang sya)
# should only contain the numbers from the input
numbers = []

# make a string containing all numbers from 0-9
all_numbers = "0123456789"

# ask the user for any input (instruction)
string = input("Please enter anything: ")

# a way to check for every character
for character in string:
    
    # check if character is found in our `all_numbers`
    if character in all_numbers:

        # append the character in the `numbers` list
        numbers.append(character)

# "".join(list_of_string)
print(numbers)
print("".join(numbers))