def main():
	person = input("What is your name? ")
	motto = input("What is your motto in life? ")
    
	with open(f"{person}.txt", "w+") as file:
		file.write(motto)
if __name__ == "__main__":
	main()