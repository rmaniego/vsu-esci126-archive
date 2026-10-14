# 4. Ask the user for his/her age
# and will determine whether he/she is a senior citizen
# (at least 60 years old) or not.

# STEPS
# 1. Ask    - What is the problem?
# 2. Find   - Gather any information that may help.
# 3. Think  - Come up with possible solutions.
# 4. Choose - Pick the best solution.
# 5. Do     - Try it and make adjustments as needed.
# 6. Code   - Convert the solution into a code.

# kinahanglan nga data
age = 0
senior_age = 60

age = int(input("What is your age? "))

if age >= senior_age:
    print("You are a senior citizen.")
else:
    print("You are not a senior citizen.")
