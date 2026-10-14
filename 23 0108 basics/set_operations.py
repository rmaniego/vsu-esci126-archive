inventory = set()

# add three items to the inventory
item = input("\nAdd item: ")
inventory.add(item)

item = input("\nAdd item: ")
inventory.add(item)

item = input("\nAdd item: ")
inventory.add(item)

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