accounts = {"Juan": 0, "Maria": 0, "Pedro": 1}

print("Inactive Accounts:")
for name, present in accounts.items():
	if present:
		continue
	print(f" * {name}")