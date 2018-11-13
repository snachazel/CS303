def main():
	import random 

	number = random.randint(0 , 100)

	print(" Guess a number between 0 and 100")

	guess = eval(input(" Enter your guess: "))

	if guess == number:
		print("correct!")
	elif guess > number: 
		print( "Too high!")
	else: 
		print("Too low!")
main()

# issues with this program are that you only get a single guess
#can change lines 11-16 to create loops so that you can get multiple guesses

#while true:
#guess = eval(input("Enter your guess:"))
#if guess == number:
#print yes the number is correct
#elif guess > number 
#print too high
#else:
# print too low

# issue here is that the loop will never end
# solution is to change the first revised line to while guess != number 