def main():
	import random

	lottery = random.randint(100 , 999)
	guess = eval(input("Enter a 3 digit lottery number:"))
	lotterydigit1 = lottery // 100
	lotterydigit2 = (lottery % 100) // 10
	lotterydigit3 = (lottery % 100) % 10
	guessdigit1 = guess // 100
	guessdigit2 = (guess % 100) // 10
	guessdigit3 = (guess % 100) % 10

	if guessdigit1 == lotterydigit1 or guessdigit1 == lotterydigit2 or guessdigit1 == lotterydigit3 or guessdigit2 == lotterydigit1 or guessdigit2 == lotterydigit2 or guessdigit2 == lotterydigit3 or guessdigit3 == lotterydigit3 or guessdigit3 == lotterydigit2 or guessdigit3 == lotterydigit3:
		print("Congratulations, your reward is $1,000!")
	elif lotterydigit1 == guessdigit1 and lotterydigit2 == guessdigit3 and lotterydigit3 == guessdigit2:
		print("Congratulations , your reward is $3,000!")
	elif lotterydigit1 == guessdigit2 and lotterydigit2 == guessdigit3 and lotterydigit3 == guessdigit1:
		print("Congratulations , your reward is $3,000!")
	elif lotterydigit1 == guessdigit2 and lotterydigit2 == guessdigit1 and lotterydigit3 == guessdigit3:
		print("Congratulations , your reward is $3,000!")
	elif lotterydigit1 == guessdigit3 and lotterydigit2 == guessdigit1 and lotterydigit3 == guessdigit2:
		print("Congratulations , your reward is $3,000!")
	elif lotterydigit1 == guessdigit3 and lotterydigit2 == guessdigit3 and lotterydigit3 == guessdigit1:
		print("Congratulations , your reward is $3,000!")
	elif guess == lottery :
		print("Congratulations, your reward is 10,000!")
	else: 
		print("Sorry, no match.")
	print(lottery)
main()	