def linearsearch(lst , key):
	for i in range(len(lst)):
		if key = lst[i]:
			return i 
	return -1

#This is massively ineffieicent as you have to iterate through every index in the list which can at worst, cause you to go through 1023 iterations beforeyou find the correct value
#on average, only have to examine half but this is still inefficient 
#elements can be in any order though 



