#  File: GuessingGame.py

#  Description: A modified binary search algorithm that will guess a number correctly in 7 tries or fewer.

#  Student Name: Stephen Nachazel

#  Student UT EID:sdn443	

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 11/12/17

#  Date Last Modified: 11/15/17

def game():
	#This initializes the lo , hi and mid so that the game can start

	turn = 1
	lo = 1
	hi = 100

	#this loop allows the user to guess a number and the algorith to adjust itself depending on its guess
	while (turn < 9 and lo <= hi):

			mid = (hi + lo) // 2
			print("Guess" , turn , ":    The number you thought was " , mid)
			guess = eval(input("Enter 1 if my guess was high, -1 if low and 0 if correct: "))
			print()
			#this loops allows for a check to make sure that the input is either -1, 0 or 1

			while guess < -1 or guess > 1:

				print("Guess" , turn , ":    The number you thought was " , mid)
				guess = eval(input("Enter 1 if my guess was high, -1 if low and 0 if correct: "))
				print()
			#These conditionls dictate what happens in the algorithm depending upon the user input
			if guess == 1:

				hi = mid - 1

				mid = (hi + lo ) // 2

				turn += 1

			if guess == -1:

				lo = mid + 1

				mid = (lo + hi ) // 2

				turn += 1

			#This conditonal is the result when the guess is correct and this breaks the loop
			if guess == 0:

				print()

				print("Thank you for playing the Guessing Game.")

				return

			#This conditional is the result of a faulty input or incorrect guess
			if turn  == 8 and guess != 0:

				print("Either you guessed a number out of range or you had an incorrect entry.")

def main():
	print()
	print("Guessing Game")
	#These lines print the head and start the game
	print()
	print("Think of a number between 1 and 100 inclusive.")
	print("And I will guess what it is in 7 tries or less.")
	print()
	ready = input("Are you ready? (y/n): ")
	print()
	#this loop checks if the first input is a y or n and repeats that question if it isn't
	while ready != "y" and ready != "n":

		ready = input("Are you ready? (y/n): ")

		print()
	#this set of condtionals gives a command depending on if the first input is a y or n
	if ready == "y":

		game()

	if ready == "n":
		
		print("Bye")
main()