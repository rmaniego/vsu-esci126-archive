# 1. Simple Interest and Future Value

# Write a Python program that computes 
# the future value of an investment using simple interest.
# The program shall accept the principal amount, interest rate, and investment duration.
# Allow the user to calculate the interest either by
# specifying the number of days (using a 360-day year) 
# or by specifying the number of periods (months or years).

# Use the following formula:
# Interest = Principal * Number of Periods * Interest Rate per Period

# Future Value = Principal + Interest

principal_amount = float(input("Enter the principal amount (Pesos): "))
interest_rate = float(input("Enter the interest rate: "))
periods = float(input("Enter the investmest period (months): "))

interest = principal_amount * periods * interest_rate
future_value = principal_amount + interest

print(f"The future value is P{future_value:,.2f} in {periods} months.")