import random

def play():
	words = open('words.txt').read().splitlines()
	chosen_word = random.choice(words)
	letters = ""
	for letter in chosen_word:
		letters += letter
	guesses = 5
	while guesses != 0:
		guess = str(input("Guess a letter: "))
		if guess in letters:
			letters = letters.replace(guess, "")
			print("You guessed a letter!")
			if len(letters) == 0:
				print("You win")
				input("Press enter to exit")
				exit()
		else:
			print("That was not a letter better luck next time")
			guesses - 1
	print("You lose :(")
			
play()
