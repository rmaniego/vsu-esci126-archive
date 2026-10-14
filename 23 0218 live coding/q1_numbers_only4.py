# 1. Ask a user any input, then remove all non-numeric characters.
#  - Examples:
#	- dh@24ohr374903jeowjr02(hjf% --> 2437490302

import re

string = input("Please enter anything: ")

numbers = re.findall(r"\d", string)

print("".join(numbers))