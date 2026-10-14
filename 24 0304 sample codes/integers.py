required = 1000

# returns a string value (numeric string)
remaining = input("Number of remaining items: ") # '36'
# print(remaining, type(remaining))
remaining = int(remaining)                       #  36
# print(remaining, type(remaining))

restock = required - remaining 

print(f"You need to restock {restock} items.")