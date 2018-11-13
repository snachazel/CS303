def listsum(l1 , l2):
	if len(l1) != len(l2):
		return False 

	if len(l1) == len(l2):
		sum = 0 
		for i in range(len(l1)):
			sum = sum + l1[i] * l2[i]

		return sum

def main():
	l1 = [ ]
	l2 = [ ]

	first = input("Enter a series of numbers seprated by a space: ")#obtains items to put into string 
	numbers1 = first.split() #extracts items from string 
	l1 = [ eval(x) for x in numbers1] #puts items into list as integers 
	second = input("Enter a series of numbers separated by a space: ")
	numbers2 = second.split()
	l2 = [ eval(x) for x in numbers2]

	print( listsum(l1, l2))

main()

