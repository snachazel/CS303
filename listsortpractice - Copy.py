def main():

	sequence = input("Enter a string of numbers: ")
	numbers = sequence.split()
	lst = [eval(x) for x in numbers]
	print(lst)

	srt = [eval(x) for x in numbers]
	srt.sort()
	print( srt)

	print( (lst == srt))


	

	
	

main()