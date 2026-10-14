inventory = []

# add three items to the inventory
item = input("\nAdd item: ")
inventory.append(item)

item = input("\nAdd item: ")
inventory.append(item)

item = input("\nAdd item: ")
inventory.append(item)

# display all items
print("\nDisplay all items:")
for item in inventory:
    print(item)

print("\nDisplay with index:")
for index, item in enumerate(inventory):
    print(index, item)

# check if item is in the inventory
item = input("\nSearch item: ")
print(f"{item} is in inventory:", (item in inventory))

item = input("\nSearch item: ")
print(f"{item} is in inventory:", (item in inventory))

# replace value in a specific
item1 = inventory[0]
inventory[0] = input(f"\nReplace 1st item: ({item1})")
print(f"Item #1 is now, ", inventory[0])

# delete an item
item = input("\nDelete item: ")
if item in inventory:
    # only remove if item exists,
    # else it will cause an error
    inventory.remove(item)
    print(f"{item} was removed from the inventory.")

# display all items
print("\nDisplay all items:")
for item in inventory:
    print(item)