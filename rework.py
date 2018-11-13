def main():

	print( "Guessing Game")

	print()
	print("Think of a number between 1 and 100 inclusive")
	print("and I will guess it in 7 tries or less")
	print()
	ready = input("Are you ready? (y/n): ")
	print()

	while ready != "y" and ready != "n":
		ready = input("Are you ready? (y/n): ")
		print()

	if ready == "y":
		turn = 1

	if ready == "n":
		print("Bye!")

main()