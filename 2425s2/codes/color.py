

def main():
    favorite = "br0wn"
    for _ in range(3):
        guess = input("\nGuess my fave color: ")
        if guess.strip().lower() == favorite:
            print("You’re right!!")
            break
        print("Incorrect, sorry...")

if __name__ == "__main__":
    main()