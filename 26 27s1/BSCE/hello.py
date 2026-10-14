def main():
    name = ""
    while not name:
        name = input("Enter your name: ").strip()
    
    print(f"\nHello, {name}!")
if __name__ == "__main__":
    main()