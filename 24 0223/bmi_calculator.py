
height_in_meters = float(input("Enter your height in meters: "))

weight_in_kg = float(input("Enter your weight in kg: "))

gender = input("Gender: (M/F) ")

bmi = weight_in_kg/(height_in_meters**2)

print(f"Your BMI is {bmi:.1f}.")

if (gender == "M" and (20 <= bmi <= 25)):
    print("You are healthy...")
elif (gender == "F" and (19 <= bmi <= 24)):
    print("You are healthy...")
elif (bmi < 20):
    print("Contact your nearest doctor...")
else:
    print("Love your body...")
