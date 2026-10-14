# 3. Construction Material Quantity Summation






# Write a Python program that accepts multiple construction material quantities
# entered as comma-separated values.
# Process each quantity and compute their total.
# The program shall display the sum of all quantities
# and the number of entries processed.



"""
Examples:
Input:  10,20,15,5
Output: Total = 50, Entries = 4

Input:  12,8,30
Output: Total = 50, Entries = 3
"""

quantities = input("Input multiple construction material quantities in CSV format: ")

total = 0
values = quantities.split(",")
for value in values:
    total += int(value)

entries = len(values)
print(f"Total = {total}, Entries = {entries}")