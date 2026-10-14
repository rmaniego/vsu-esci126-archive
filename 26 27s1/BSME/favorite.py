def main():
    color = "kahel"
    for _ in range(3):
        guess = input("\nGuess my fav color: ")
        if guess.strip().lower() == color:
            print("You’re right!!")
            break
        print("Incorrect, sorry...")
    
if __name__ == "__main__":
    main()