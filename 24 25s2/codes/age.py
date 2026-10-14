

def main():
    age = int(input("Enter age: "))
    if age < 0:
        print("Invalid input.")
    elif age < 18:
        print("You are still a Minor.")
    elif age >= 60:
        print("You are a Senior Citizen.")
    else:
        print("You are an Adult.")

if __name__ == "__main__":
    main()