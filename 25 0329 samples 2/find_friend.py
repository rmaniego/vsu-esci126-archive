

def main():
    friend = input("Which friend? ")
    
    with open(f"{friend}.txt", "r") as file:
        message = file.read()
        print(message)

if __name__ == "__main__":
    main()