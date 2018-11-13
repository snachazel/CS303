
#  File: Grid.py

#  Description: A program that calculates the largest subproduct for a square matrix of dimension greater than 4.

#  Student Name: Stephen Nachazel

#  Student UT EID:sdn443

#  Partner Name: none

#  Partner UT EID: none

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created:10/25/17

#  Date Last Modified: 11/3 /17


#This function returns all the subproducts of 4 integers for each row in the 2D list
def rowProducts(grid , i , j):

	#This conditional is to make sure that the values in the rows do not extend past the boundary of the matrix
	if (j < len(grid) -3):

		rowSubProduct = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]

		return (rowSubProduct)
	else:
		return 0


#This function returns all of the 4 integer subproducts in eac of the columns of the matrix
def columnProducts( grid , i , j ):

	if (i < len(grid) - 3):

		colSubProduct = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]

		return (colSubProduct)
	else:
		return 0


#this function is meant to record all 4 number subproducts in the right to left diagonals throughout the matrix
def diagonalProducts1(grid , i , j):

	if (i < len(grid) -3 and j < len(grid) - 3):

		rightLeftProduct = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][ j + 3]

		return(rightLeftProduct)
	else: 
		return 0

#this function is meant to record all of the 4 integer subproducts along the left to right diagonals 
def diagonalProducts2(grid , i , j):

	if (i < (len(grid)  - 3) and int(j) >= 3) :

		leftRightProduct = grid[i][j] * grid[i+1][j-1] * grid[ i + 2 ][j - 2] * grid[i + 3 ][j -3 ]

		return(leftRightProduct )
	else:
		return 0
	


def main():
	#This opens the file that we want to read
	in_file = open("./grid.txt" , "r")

	#This section of code obtains the dimension of the list, which is the number of rows and columns here since we only have square matrices as 2D lists 
	dim = in_file.readline()
	dim = dim.strip()
	dim = int(dim)

	#Here, empty lists are created in order to populate them with what we want
	grid = []
	products = []

	#This for loop populates grid with n = dim lists each of which have n = dim elements in them
	for i in range(dim):

		line = in_file.readline()

		line = line.strip()

		row = line.split()

		for j in range(dim):

			row[j] = int(row[j])

		grid.append(row)

	#here we close the file we read in.
	in_file.close()

	#Using the user defined functions, all 4 integer subproducts are computed and put into the second empty list
	#the outer loop handles the row number while the inner loop handles the column number
	for i in range(dim):

		for j in range(dim):

			products.append(int(rowProducts(grid , i , j)))

			products.append(int(columnProducts(grid , i , j)))

			products.append(int(diagonalProducts1(grid , i , j)))

			products.append(int(diagonalProducts2(grid , i , j)))

	#This returns the largest number in the list of products and then prints it out.
	large = max(products)
	print("The greatest product is ",large, ".")
	
main()
