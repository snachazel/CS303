#  File: Goldbach.py

#  Description: A program that displays the results of the Goldbach conjecture for integers in a given range.

#  Student Name:Stephen Nachazel

#  Student UT EID:sdn443

#  Course Name: CS 303E

#  Unique Number: 53140

#  Date Created:10/8/17

#  Date Last Modified:10/9/17

def main():

  #This section of the code is to set the bounds for the Goldbach sequence 
  lower_limit = eval(input("Enter the lower limit:"))

  upper_limit = eval(input("Enter the upper limit:"))

  while (lower_limit < 4) or (lower_limit % 2 != 0 or upper_limit % 2 != 0) or (lower_limit > upper_limit):

  	lower_limit = eval(input("Enter the lower limit:"))

  	upper_limit = eval(input("Enter the upper limit:"))


  #This section of the code is to calculate the different pairs of primes for each even value of n
  #This outer loop is used to start off each row with a positive number in the defined range
  for n in range( lower_limit , upper_limit + 1):

  	if n % 2 == 0:

  		print( n , end = ' ')

  	#This inner loop is to check for pairs of prime numbers that sum to the even value of n
  	for i in range( 2 , (n // 2) +1):

  		a = i

  		b = n - a

  		if is_prime(a) and is_prime(b) and n % 2 == 0:

  			print( "=" ,a , "+" , b, end = ' ')

  		i += 1

  	n += 1

  	print()
  #This section of code is using the in class is_prime function in order to determine the primacy of a and b as defined in the loop above.
def is_prime(n):

  limit = int (n ** 0.5) + 1

  div = 2

  while (div < limit):

    if (n % div == 0):

      return False

    div += 1

  return True

main()


  



