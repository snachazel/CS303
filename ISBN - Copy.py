#  File: ISBN.py

#  Description: A program that tells if a string is a Correct ISBN or not.

#  Student Name:Stephen Nachazel

#  Student UT EID: sdn443

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 10/25/17

#  Date Last Modified:10/30/17

def is_valid(isbn):
	#This is section of the code is to initialize the lists that will be used to calculate partial sums
	isbnList = []

	s1 = []

	s2 = []
	
	#this section is to get the lines from the in file to a format whee they are easily readable 
	isbn = isbn.upper()

	isbn = isbn.strip("\n")

	isbn = isbn.replace("-" , "")

	#This loop runs the checks of making sure the string length is 10, checking for only the correct characters, and then creating the proper lists to calculate the sums
	for i in range(len(isbn)):

		if ((isbn[i] != "X") and (isbn[i] != "-")) and (( int(ord(isbn[i]) < 48) or (int(ord(isbn[i]))> 57))):

			return False 

		if (( i != (len(isbn) - 1)) and (isbn[i] == "X")) : 

			return False

		elif (ord(isbn[i]) >= 48) and (ord(isbn[i]) <= 57):

			isbnList.append(eval(isbn[i]))

		elif( isbn[i] == "X"):

			isbnList.append(10)

	if len(isbn) != 10:

			return False 

		
	#this loops initializes the lists and then calculates the requisitie partial sums 
	for i in range(0 , len(isbnList)):

		s1.append(0)

		s2.append(0)
	
		for j in range(0 , i + 1):

			s1[i] += int(isbnList[j])

		for j in range(0 , i + 1):

			s2[i] += int(s1[j])

	#this checks if the last term in s2 is divisible by 11 and returns true or false 
	if s2[9] %11 == 0:

		return True 
#Main here opens the input file and output file and then writes the output file telling us if the ISBNs are valid or invalid 
def main():
	rawISBN = open ( "./isbn.txt" , "r")

	validISBN = open("./isbnOut.txt" , "w")

	for isbn in rawISBN:

		if is_valid(isbn):

			validISBN.write(str(isbn).strip() + "  valid\n")

		else:

			validISBN.write( str(isbn).strip() + "  invalid\n")

	#this closes the output and input files explicitly 
	rawISBN.close()
	validISBN.close()
main()





