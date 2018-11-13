def main():
	print("             Multiplication Table") # table title 
	print("    |", end = '')
	for j in range(1 , 10): #this loop prints the numbers that would be across the top
		print(" ", j, end = ' ')
	print() # jumpt to new line
	print("-------------------------------------------")

	#display table body
	for i in range( 1 , 10): #this loop provides the column names and then also the outer loop for the inner loop to be multiplied by to produce the right product
		print( i , "|" , end = ' ')
		for j in range(1, 10):
			#display product and align properly
			print(format( i * j , "4d") , end = '') # end = ' ' allows the print function to remain on the same line to produce each line 
		print() # jump to new line 
main()