#This is importing two libraries so that their functions can be useed
import math
import random

#This function uses Monte Carlo Methods to determine the experimental calculation of PI
def computePI(numThrows):
  #initializing both counts
  total_throws = 0

  successful_throws = 0

  #the while loop conducts all of the trials within the range
  while total_throws <= numThrows:

  	xPos = random.uniform( -1.0 , 1.0 )

  	yPos = random.uniform( -1.0 , 1.0 )

  	distance = math.hypot(xPos , yPos)

  	#this conditional records successful throws by checkin if they are in the correct region
  	if distance < 1 :

  		successful_throws += 1

  	total_throws += 1

  ratio = successful_throws / numThrows

  calculatedPI = 4 * ratio

  #This function returns only one value which will be used in main()
  return calculatedPI
  	

def main():

  #Using the return value from computePi , main prints the value of pi, trials and error for 6 different trial runs 
  
  print("Computation of PI using Random Numbers")
  print("")

  for i in [ 100, 1000, 10000, 100000, 1000000 , 1000000]:
    print(format(("num = " , i) , "<17s") , end = " ")
    print("Calculated PI =", format( computePI(i) , "7.6f") , end = " ")
    print ( "Difference =" , "{0:+f}".format( computePI(i) - math.pi,  "7.6f"))

main()