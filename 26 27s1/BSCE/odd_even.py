

def main():
    # ask for two numbers
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    
    # compute the result
    result = number1 % number2
    
    # display the result
    print(f"{number1} % {number2} = {result}")


if __name__ == "__main__":
    main()