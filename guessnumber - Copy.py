def main():
	import random

	number = random.randint(0 , 100)

	print("Guess a magic number between 0 and 100")

	#the reason that guess is initialized to -1 is so that it starts at a number that is not an answer 
	guess = -1
	#loop starts here 
	while guess != number:

		guess = eval(input("Enter your guess:"))

		if guess == number:
			print("Correct!")
		elif guess > number:
			print("Too high!")
		else:
			print("Too low!")

main()