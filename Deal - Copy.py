# File: Deal.py

# Description: A program that simulates the Monty Hall Problem using random numbers and for loops

# Student Name: Stephen Nachazel

# Student UT EID: sdn443

# Course Name: CS 303E

# Unique Number: 51340

# Date Created: 10/ 15/ 17

# Date Last Modified: 10 /20 /17

import random
import math 

import random
import math 

def main():
  #this section of the code is to obtain the number of trials that the user wants to run 
  numTrials = eval( input("Enter number of times you want to play: "))
  print()
  #this is to initializa the counter for wins from switching 
  switchWins = 0
  print("  Prize      Guess       View    New Guess ")
  #this for loop is for determing guess , prize , view and new guess using a combination of random numbers and determinisitc processes 
  for i in range( 0 , numTrials + 1):
  	prize = random.randint( 1 , 3 )
  	guess = random.randint( 1 , 3 ) 
  	if prize == 1 and guess == 3:
  		view = 2 
  	if prize == 1 and guess == 2:
  		view = 3 
  	if prize == 2 and guess == 3:
  		view = 1 
  	if prize == 2 and guess == 1:
  		view = 3 
  	if prize == 3 and guess == 1:
  		view = 2 
  	if prize == 3 and guess == 2:
  		view = 1
  	if prize == guess :
  		view = (prize % 3) + 1

  	if guess == 1 and view == 2:
  		newGuess = 3 
  	if guess == 2 and view == 1:
  		newGuess = 3
  	if guess == 2 and view == 3:
  		newGuess = 1
  	if guess == 1 and view == 3:
  		newGuess = 2
  	if guess == 3 and view == 2:
  		newGuess = 1
  	if guess == 3 and view == 1:
  		newGuess = 2 

  	if newGuess == prize:
  		switchWins += 1
  		#this is to keep track of the wins from switching doors
  	print ("   " ,prize,"        ", guess ,"        ", view , "        ", newGuess) 

  #this is computing and printing the probabilities that should converge to 2/3 and 1/3 
  switchProbability = switchWins / numTrials
  noSwitch = 1 - switchProbability

  print()
  print("Probability of winning if you switch =", format(switchProbability , ".2f"))
  print("Probability of winning if you do not switch = " , format(noSwitch , ".2f"))
main()


