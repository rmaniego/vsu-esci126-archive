# 1. Simple Interest and Future Value

# Write a Python program that computes 
# the future value of an investment using simple interest.
# The program shall accept the principal amount, interest rate, and investment duration.
# Allow the user to calculate the interest either by
# specifying the number of days (using a 360-day year) 
# or by specifying the number of periods (months or years).

# Use the following formulas:
# Interest = Principal * (Number of Days / 360) * Annual Interest Rate
# Interest = Principal * Number of Periods * Interest Rate per Period

# Future Value = Principal + Interest

principal_amount = float(input("Enter the principal amount (Pesos): "))
interest_rate = float(input("Enter the interest rate: "))
investment_duration = int(input("Enter the investmest duration (days): "))

interest = principal_amount * (investment_duration / 360) * interest_rate
future_value = principal_amount + interest

print(f"The future value is P{future_value:,.2f}.")