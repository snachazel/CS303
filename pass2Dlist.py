def getMatrix():
	matrix = []
	# creates an empty lists

	numberOfRows = eval(input("Enter the number of rows: ")) #gives the number of elements in the initial list which is the rows in the corresponding matrix
	numberOfColumns = eval(input("enter the number of columns: "))#gives the number of elements in the corresponding 
	for row in range(numberOfRows):
		matrix.append([])#adds an empty new row
		for column in range(numberOfColumns):
			value = eval(input("Enter a value and press enter: "))#this gives a value for each place in the list 
			matrix[row].append(value) # this appends each value to the [i][j] entry in the list 

	return matrix 

def accumulate(m):
	total = 0 
	for row in m: 
		total += sum(row)

	return total 

def main():
	m = getMatrix()#creates a list 
	print(m)

	print("\n Sum of all elements is" , accumulate(m))

main()