def main():
	allowances = {
        "Juan": 100,
        "Maria": 150,
        "Pedro": 5,
        "Elmer": 1000,
        "Jermaine": 5000,
        "Junjun": -500
    }
    
	print("Allowance:")
	for name, allowance in allowances.items():
		print(f" * {name} = {allowance}")
if __name__ == "__main__":
	main()