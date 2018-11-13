def getGrade(score):
	if score >= 90.0:
		return 'A'
	if score >= 80.0:
		return 'B'
	if score >= 70.0:
		return 'C'
	if score >= 60.0:
		return 'D'
	else:
		return 'F'
def main():
	score = eval(input("Enter a score: "))
	print("The grade is" , getGrade(score))

main()

# notice that usine getgrade returns some value which can be used to print a result in main