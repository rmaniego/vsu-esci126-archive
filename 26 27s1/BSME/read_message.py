def main():
	person = input("What is your name? ")
    
	with open(f"{person}.txt", "r") as file:
		print(file.read())
		
if __name__ == "__main__":
	main()