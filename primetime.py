def main():
	numberofprimes = 50
	numberofprimesperline = 10 
	count = 0 # count number of prime numbers
	number = 2 # number to be test for primeness

	print( "The first 50 primes are")

	while count < numberofprimes :
		#assume the number is prime
		isprime = True # is current number prime 

		divisor = 2 
		while  divisor <= number / 2:
			if number % divisor == 0:
				# if true, not prime
				isprime = False
				break
			divisor += 1
			
	if isprime:
		count += 1 

		print(format(number, "5d") , end = ' ')
		if count % numberofprimesperline == 0:
			print( )
	number += 1 
main()