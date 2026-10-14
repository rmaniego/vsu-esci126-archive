# 2. Ask a valid credit card number, then replace all digits with asterisks (*) except the last four digits.
# - 13, 16, or 19 digits, dashes are allowed.
# - display errors when necessary.
# - Examples:
#	- 1111-2222-3333-4444 --> ****-****-****-4444
#	- 1111222233334444 -->	************4444

"""
Sample Solution:
1. Remove all non-numeric characters.
2. Check if the remaining characters truly a valid digit.
3. Check if the length of the CC No. is 13, 16, or 19 digits
4. Get the last 4 digits.
5. Get the first N-4 digits, then mask items
6. Print the masked digits and the last 4 digits.
"""


card_number = input("Enter your credit card number: ")
cleaned_card_number = card_number.replace("-", "")

if cleaned_card_number.isdigit():
    # check if length = 13, 14, 19
    if len(cleaned_card_number) in (13, 16, 19):
        last_four_digits = cleaned_card_number[-4:]
        digits_to_be_masked = cleaned_card_number[:-4]
        
        masked_credit_card_number = "*" * len(digits_to_be_masked)
        masked_credit_card_number += last_four_digits

        print(f"Error: Your credit card number is: {masked_credit_card_number}")
    else:
        print("Error: Credit card number must be 13, 15, or 19 digits only.")
else:
    print("Error: Your credit card is invalid.")