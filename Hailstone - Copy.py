#  File: Hailstone.py

#  Description: A program calculating the cycle length for the Collatz sequence

#  Student Name: Stephen Nachazel

#  Student UT EID:sdn443

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 9 /26 /17

#  Date Last Modified: 9 /28/17

def main():
  
  #This section of the code is to obtain the range values and run a check to make sure they are positive and in ascending order.

  a = eval(input("Enter the starting number of the range: "))

  while a < 1:
  	a = eval(input("Enter the starting number of the range: "))

  b = eval(input("Enter the ending number of the range: "))

  while b< 1:
  	b = eval(input("Enter the ending number of the range: "))

  if a >= b:
  	a , b = b , a 
  
  #This section of the code is computing the number of steps in the Collatz sequence for each number in the Range. 
  sequence_steps = 0 

  for n in range( a , b + 1):
  	i = n
  	count = 0 

  	while i > 1:

  		if i % 2 == 0:
  			i = i // 2
  			count += 1

  		else: 
  			i = 3 * i + 1
  			count += 1

    #This section of the code is for determining which number has the longest sequence and the storing that variable. 
  	if (count >= sequence_steps):

  		sequence_steps = count

  		longest_cycle = n

  n = longest_cycle

  #This section of the code is for displaying the results of the program.
  print(" ")

  print("The number" , n , "has the longest cycle length of" , sequence_steps ,".")

main()

