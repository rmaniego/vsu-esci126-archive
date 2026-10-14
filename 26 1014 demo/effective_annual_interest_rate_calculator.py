# 1. Effective Annual Interest Rate

# Write a Python program that computes the effective annual interest rate
# based on a given nominal interest rate and compounding frequency.


# The program shall allow the user to select from
# daily (365),
# monthly (12),
# every two months (6),
# quarterly (4),
# semi-annually (2),
# or annually (1).
# Compute and display the effective annual interest rate
# using the following formula:

# Effective Annual Rate = (1 + Nominal Rate / Periods per Year) ** Periods per Year - 1

print("OPTIONS:")
print(" 1 - Daily")
print(" 2 - Monthly")
print(" 3 - Every two months")
print(" 4 - Quarterly")
print(" 5 - Semi-annually")
print(" 6 - Annually")

compounding_frequency = int(input("Choose your preferred compounding frequency: "))

period = 0
if compounding_frequency == 1:
    period = 365
elif compounding_frequency == 2:
    period = 12
elif compounding_frequency == 3:
    period = 6
elif compounding_frequency == 4:
    period = 4
elif compounding_frequency == 5:
    period = 2
elif compounding_frequency == 6:
    period = 1

if period == 0:
    print("Choice is not in the options.")
else:
    # continue the calculation
    nominal_interest_rate = float(input("\nEnter the nominal interest rate: "))
    effective_annual_rate = (1 + nominal_interest_rate / period) ** period - 1
    
    print(f"\nThe effective interest rate is {effective_annual_rate:.2f}.")
    
