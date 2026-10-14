# 1. Ask a user any input, then remove all non-numeric characters.
#  - Examples:
#	- dh@24ohr374903jeowjr02(hjf% --> 2437490302

# create an empty string variable
numbers = ""

# ask the user for any input
string = input("Please enter anything: ")

# to be able to check every character
# I need to loop over the string variable
for character in string:
    
    # I will check whether the character is a number
    # using the `.isdigit()` method --> 0123456789
    # Example: dh@24
    if character.isdigit():
        # If character is numeric
        # I will `append` the character in the number `variable`
        numbers += character

# just printing the value of `numbers` variable
print(f"Numbers only: {numbers}")



