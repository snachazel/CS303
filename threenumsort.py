def main():
	
	nums= (input("Enter three numbers:"))
	spt = nums.split()
	lst = [eval(x) for x in spt]
	print( spt )

	if spt[0] < spt[2] < spt[1]:
		nspt= []
		nspt.append(spt[0])
		nspt.append(spt[2])
		nspt.append(spt[1])
		print(nspt)


	
main()


