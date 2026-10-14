# 5. List: Built-in Functions

# variable.method() --> ex. list methods
# function(variable)

currencies = ["PHP", "USD", "EUR", "CNY", "JPY", "HKD", "AUD", "PHP", "EUR", "CHF", "AMD"]
print(f"\n{currencies = }")

# count the number of items
count = len(currencies) # length
print(f"\n{count = }")

# not in-place sorting
# NOTE: this will create a new list
#       useful when you don't want to change the original list
sorted_currencies = sorted(currencies)
# print(f"\n{currencies = }")
print(f"\n{sorted_currencies = }")


# reversing a list, not necessarily sorting
# NOTE: this will create a new list
#       useful when you don't want to change the original list
reversed_currencies = list(reversed(currencies))
print(f"\n{reversed_currencies = }")

sorted_currencies = sorted(currencies)
reversed_sorted_currencies = list(reversed(sorted_currencies))
print(f"\n{reversed_sorted_currencies = }")

# get unique items --> very fast
# 1. Cast list to set "only unique items"
# 2. Cast set back to list
unique = list(set(currencies))
print(f"\n{unique = }")

## sorting it
unique = sorted(list(set(currencies)))
print(f"\n{unique = }")