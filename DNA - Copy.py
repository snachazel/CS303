#  File: DNA.py

#  Description: A program that searches for and displays matching DNA substrands 

#  Student Name: Stephen Nachazel

#  Student UT EID: sdn443

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 10 / 22 /17

#  Date Last Modified: 10/ 26 /17
def main():

	print("Longest Common Sequences")
	print("")

	in_file = open("./dna.txt" , "r")

	num_pairs = in_file.readline ()
	num_pairs = num_pairs.strip ()
	num_pairs = int( num_pairs)

	#This section of code reads in pairs of lines, strips spaces, and turns them all upper case in order to easily compare them 
	for i in range( num_pairs):

		st1 = in_file.readline()
		st2 = in_file.readline()

		st1 = st1.strip()
		st2 = st2.strip()

		st1 = st1.upper()
		st2 = st2.upper()

		#This list is created in order to have a place to store each of the longest common Strands 
		commonStrands = [] 

		#This section of code is making sure that the shorter line of DNA is always st2

		if (len(st1) > len(st2)):
			dna1 = st1
			dna2 = st2

		else:
			dna1 = st2
			dna2 = st1

		#this is the strand that the program is trying to find in the lponger strand, st1
		wnd = len (dna2)

		#This loop tells the program to cease going through the loop once the longest substrings are found 
		while (wnd > 1):
			start_index = 0 
			if len(commonStrands) > 0:
				break
			#this loop handles searching for common strands and adjusting the search window size
			while( (wnd + start_index) <= len(dna2)):

				sub_strand = dna2[start_index: start_index + wnd]

				if sub_strand in dna1:

					commonStrands.append(sub_strand)

				else:

					pass

				start_index += 1

			wnd = wnd - 1


		#This section of the Code is formatting the output so that all Subsequences are properly aligned vertically 
		
		print("Pair" ,i + 1, ":" , end = "")

		#This nested conditional handles the initial returned value and then any subsequent returned values depending on their stored position in the created list
		if len(commonStrands) == 0:
			print("No Common Sequence Found")
		else:
			for i in range(0 , len(commonStrands)):
				if i == 0: 
					print (commonStrands[i])
				else:
					print( "        " + commonStrands[i])
	in_file.close()
main()