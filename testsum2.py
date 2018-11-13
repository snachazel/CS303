def main():
	sum = 0 
	#initializing the sum

	count = 0
	i = 0.01
	while count < 100:
		sum += i
		# assignment operator
		i = i + 0.01
		count += 1
		# changing the value of a variable 
		#need the count so that the program increases the ocunt and eventually ends 

	print("The sum is ", sum)
main()