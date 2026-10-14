def main():



    dividend = float(input("Dividend: "))
    divisor = float(input("Divisor: "))
    try:
        quotient = dividend / divisor
        print(f"Result: {quotient:.2f}")
    except ZeroDivisionError as e:
        print("Warning: Divisor must be greater than 0.")
if __name__ == "__main__":
    main()