# 2. Soil Subgrade Classification

# Write a Python program that determines the soil subgrade classification
# based on its California Bearing Ratio (CBR). 
# The program shall accept the CBR value as a percentage 
# and display the corresponding classification 
# according to the following simplified scale:

# CBR Value	Classification
# ≥ 20%	Very Good
# ≥ 10%	Good
# ≥ 5%	Fair
# ≥ 3%	Poor
# < 3%	Very Poor

cbr = float(input("Enter the CBR value: "))

if cbr >= 20:
    print("Very Good")
elif cbr >= 10:
    print("Good")
elif cbr >= 5:
    print("Fair")
elif cbr >= 3:
    print("Poor")
else:
    print("Very Poor")