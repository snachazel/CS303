def main():
	year = eval(input("Enter a year: "))

	#this is a boolean expression with two nested statements so only one needs to be true but both can be 
	#such statments evaluate to either true or false 
	isLeapyear = ( year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0)

	print( year , "is a leap year?" , isLeapyear)

main()