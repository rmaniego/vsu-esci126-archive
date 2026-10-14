# 4. Basic List Methods

# hardcoded - manually written in the program
# programmatically - created/modified through 'operations'

# Modifying a list programmatically
# - meaning not hardcoded values...

# Starting empty list
items = []

# Add new item - methods or operations
items.append("Juan")
items.append("Pedro")
items.append("Pedro")
items.append("Maria")
items.append("Pedro")
items.append("Clara")
items.append("Pedro")
items.append("KimChew")


print(f"\n{items = }")

# Insert at a specific index
# NOTE: If index is bigger than the actual list,
#       then it will work like append.
# inserts at index 0, 1
items.insert(0, "Dominador")
items.insert(1, "Pedro")

print(f"\n{items = }")

# Count the occurrence of an item
search = "Pedro"
count = items.count(search)
print(f"\n{search} = {count}")

search = "Julia"
# list_variable.count(search_item)
count = items.count(search)
print(f"\n{search} = {count}")

# Sorting "in-place"
# Meaning it will sort the list, not create a new list in the memory
# This is light way to sort a list versus other ways
items.sort()
print(f"\nSorted = {items}")

# Sorting and reversing at the same time
items.sort(reverse=True)
print(f"\nSorted (reverse) = {items}")

# Remove specific item
# NOTE: Removing an item that does not exists will cause an error.
#       Removing an item with duplicates, will only remove the first occurrence.
# remove existing item
items.remove("Pedro")
print(f"\n{items = }")

# Remove all duplicates: Option #1
# slow method
search = "Pedro"
while items.count(search) > 1:
    items.remove(search)
print(f"\n{items = }")

# Remove at specific index
# NOTE: If the specified index is larger that the actual list,
#       then it will cause an error.
# remove item using the index

removed = items.pop(0)
print(f"\n{removed = }")
print(f"{items = }")

# Clearing a list
# This will free up the RAM space automatically, very useful on very large lists.
# Meaning your PC will less likely to slow down during the execution.
items.clear()

print(f"\n{items = }")