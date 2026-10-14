# Problem:  Write a Python program that will ask a number
#           from the user and will display its factors.

number = int(input("Enter a number: "))

for i in range(1, number+1):
    # de-nesting
    if (number % i):
        continue
    print(i)