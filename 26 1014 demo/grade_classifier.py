# Grade Classification

# Write a Python program that determines 
# the equivalent grade classification based on a student's numerical grade.
# The program shall accept a grade expressed as a percentage
# and display its corresponding classification 
# according to the following scale:

# Grade	Classification
# ≥ 98%	Excellent
# ≥ 95%	Highly Outstanding
# ≥ 92%	Outstanding
# ≥ 89%	Very Good
# ≥ 86%	Good
# ≥ 83%	Very Satisfactory
# ≥ 80%	Satisfactory
# ≥ 77%	Fair
# ≥ 75%	Passing
# < 75%	Failed

grade = float(input("Enter your GWA: "))

if grade >= 98:
    print("Excellent")
elif grade >= 95:
    print("Highly Outstanding")
elif grade >= 92:
    print("Outstanding")
elif grade >= 89:
    print("Very Good")
elif grade >= 86:
    print("Good")
elif grade >= 83:
    print("Very Satisfactory")
elif grade >= 80:
    print("Satisfactory")
elif grade >= 77:
    print("Fair")
elif grade >= 75:
    print("Passing")
else:
    print("Failed")