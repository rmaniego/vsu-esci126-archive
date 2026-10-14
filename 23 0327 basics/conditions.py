# Create a Python program
# that will display the equivalent grade.

"""
above or equals to 90% : Grade A
above or equals to 80% : Grade B
above or equals to 70% : Grade C
above or equals to 60% : Grade D
above or equals to 40% : Grade E
less tha 40% : Grade F
"""

grade = float(input("Enter your numeric grade: "))

if grade >= 90:
    print("Grade A")
elif 80 <= grade < 90:
    print("Grade B")
elif 70 <= grade < 80:
    print("Grade C")
elif 60 <= grade < 70:
    print("Grade D")
elif 40 <= grade < 60:
    print("Grade E")
else:
    print("Grade F")
    
    
    
    
    
    