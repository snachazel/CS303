def main():
	import random

	lottery = random.randint(0 ,99)

	#user needs to enter a guess for the lottery
	guess = eval(input(" Enter a two digit number to pick for the lottery: "))

	#get digits from lottery 
	lottery1 = lottery // 10
	lottery2 = lottery % 10

	#get guess digits
	guess1 = guess // 10
	guess2 = guess % 10

	print("The lottery number is" , lottery)

	#check guess
	if guess == lottery:
		print("Exact match, you win $10,000!")
	elif( guess2 == lottery1 and guess1 == lottery2):
		print("All digits match, you win $3,000!")
	elif(guess1 == lottery1 or guess1 == lottery2 or guess2 == lottery1 or guess2 == lottery2):
		print("Match one digit, you win $1,000!")
	else:
		print("Sorry no match.")
	# using elif function here allows for there to be multiple if statements written quickly
	#if-elif- else statemnts need 1 if, as many elif as needed, and 1 else statment to finish it off
	
main()