#Guess a number

import random


def guess(x):
	random_number = random.randint(1, x)
#we don't want the guess to equal the random number
	guess = 0
	while guess != random_number:
		guess = int(input(f'\nGuess a number between 1 and {x}: '))
		if guess < random_number:
			print('Guess again!. Too low!')
		elif guess > random_number:
			print("Guess again!. Too High")
	print(f'Yay, congrats. You have guessed the number {random_number} corectly!')

	
guess(10)