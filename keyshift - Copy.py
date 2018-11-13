def rotate( str, key):
	for i in range(len(str)):
		j = (i - key) % ( len(str) )
		print(str[j] , end = " ")

def main():
	str = input("Enter a string: ")
	key = eval(input("Eeter a rotation parameter: "))

	(rotate(str , key))
main()
