inventory = {}

# method #1: add items to the inventory
item = input("\nAdd item: ")
count = int(input(f"Number of {item}: "))
inventory.update({item: count})

# method #2: add items to the inventory
item = input("\nAdd item: ")
count = int(input(f"Number of {item}: "))
inventory[item] = count

# display all items
print("\nDisplay all items:")
for item, count in inventory.items():
    print(item, count)

# check if item is in the inventory
item = input("\nSearch item: ")
print(f"{item} is in inventory:", (item in inventory))

item = input("\nSearch item: ")
print(f"{item} is in inventory:", (item in inventory))

# update value of an item
item = input("\nSearch item: ")
inventory[item] = input(f"Update {item} count: ")
print(f"{item} count:", inventory[item])

# delete an item
item = input("\nDelete item: ")
if item in inventory:
    # only remove if item exists,
    # else it will cause an error
    del inventory[item]
    print(f"{item} was removed from the inventory.")

# display all items
print("\nDisplay all items:")
for item, count in inventory.items():
    print(item, count)