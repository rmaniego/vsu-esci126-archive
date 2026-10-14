try:
    dividend = float(input("Dividend: "))
    divisor = float(input("Divisor: "))
except:
    print("Invalid input.")

try:
    quotient = dividend / divisor
    print(f"Result: {quotient:.2f}")
except ZeroDivisionError as e:
    print("Value must be > 0")