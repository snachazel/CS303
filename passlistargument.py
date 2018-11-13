def main():
	x = 1 
	y = [ 1 , 2 , 3 ]

	m(x,y)

	print(x, "is" , x)
	print("y[0] is " , y[0])

def m(number, numbers):
	number = 1001
	numbers[0] = 5555
main()
# y and numbers refer to the same element therefore it is possible to alter y by altering numbers
# however, number is immutable so it can't be changed and the original instance outside the function can't be changed so x is still 1 
