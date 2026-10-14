def main():
    
    
    
    
    # number = int(input("Enter a number: "))
    try:
        number = int(input("Enter a number: "))
    except ValueError as e:
        print("Value must be an integer.")
if __name__ == "__main__":
    main()