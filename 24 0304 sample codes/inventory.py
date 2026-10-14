inventory = {
        "Screw": 5,
        "Hammer": 1,
        "Plywood": 12,
        "Cement": 5,
        "Power drills": 6,
        "Steel-toe boots": 24
    }

print("My Inventory:")

# for key, value on dictionary
for item, count in inventory.items():
	print(f" - {item} x{count}")