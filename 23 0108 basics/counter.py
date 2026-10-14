# Problem:  Write a Python program that will count from 1 to 10
#           while displaying both the previous number
#           and the current number at each iteration.

previous = 0
for number in range(1, 11):
    if previous:
        print(f"{previous}, {number}")
        previous = number
        continue
    print(number)
    previous = number