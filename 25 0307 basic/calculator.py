
def adder(number1, number2):
	return number1 + number2

def subtractor(number1, number2):
	return number1 - number2

def multiplier(number1, number2):
	return number1 * number2

def divider(number1, number2):
	return number1 / number2

def main():
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    result1 = adder(number1, number2)
    result2 = subtractor(number1, number2)
    result3 = multiplier(number1, number2)
    result4 = divider(number1, number2)
    
    print(f"The sum of {number1} and {number2} is {result1}.")
    print(f"The difference of {number1} and {number2} is {result2}.")
    print(f"The product of {number1} and {number2} is {result3}.")
    print(f"The quotient of {number1} and {number2} is {result4}.")

if __name__ == "__main__":
	main()
    
