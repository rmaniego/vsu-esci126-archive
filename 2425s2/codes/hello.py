

def main():
    name = ""
    while name == "":
        name = input("Enter your name: ").strip()
    
    print(f"\nHello, {name}!")

if __name__ == "__main__":
    main()