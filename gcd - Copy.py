def main():
	#prompt user to enter 2 values
	n1 = eval(input( "Enter first integer: "))
	n2 = eval(input("Enter Second Integer: "))

	gcd = 1
	#initializing the GCD
	k = 2
	while k <= n1 and k <= n2:
		if n1 % k == 0 and n2 % k == 0:
			gcd = k
			# renaming the GCD so that it can increase 
		k += 1 
		#increasing the constant so that the next GCD is tried
	print("The GCD for" , n1 , "and" , n2 , "is " , gcd)
main()