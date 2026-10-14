fave_color = "blue"
for _ in range(3):
	guess = input("\nGuess my fave color: ")
	if guess.strip().lower() == fave_color:
		print("You’re right!!")
		break
	print("Incorrect, sorry...")