inventory = {
                "Screw": 5,
                "Hammer": 1,
                "Plywood": 0,
                "Cement": 150,
                "Lansang 1\"": 20,
                "Steel Bar": 0,
            }

print("My Inventory:")
for item, count in inventory.items():
	print(f" - {item} x{count}")