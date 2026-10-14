# Problem:  Write a Python program that will ask the user for his/her age
#           and will determine whether he/she is a senior citizen
#           (at least 60 years old) or not.

age = int(input("What is your age? ").strip())

if age >= 60:
    print("You are a senior citizen.")
else:
    print("You are not a senior citizen.")