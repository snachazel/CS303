def main():
	key = [ "blue" , " pink"]
	entry = []

	infile = open("./fruit.txt" , "r")
	length = infile.readline()
	length = length.strip()
	length = int(length)
	for i in range( length):
		line = infile.readline()
		line = line.strip()
		entry.append(line)

	for i in key:
		if i in entry and i in key:
			print("False")
			break
		else:
			print("True")
	
	
	
	print(entry)
	print(key)


main()
	
