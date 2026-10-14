

def main():
    friend = input("Who are you? ")
    
    with open(f"{friend}.txt", "w+") as file:
        file.write(f"Hello, {friend}!")

if __name__ == "__main__":
    main()