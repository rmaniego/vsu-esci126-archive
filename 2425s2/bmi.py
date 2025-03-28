
# 3. Write a simple Python program 
# that will ask the user weight (kg)
# and height (m),
# then will compute his Body Mass Index.
# Formula: BMI = kg/m²

def main():
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    
    bmi = weight / (height**2)

    print(f"Your BMI is {bmi:.2f}.")

if __name__ == "__main__":
    main()