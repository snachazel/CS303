def main():


	s = input("enter a string of numbers: ")
	nums = s.split()
	l1 = [ eval(x) for x in nums]
	print(l1)
	l1.sort()
	print(l1)
	for i in l1:
		while l1.count(i) > 1:
			l1.remove(i)
	print( l1 )
main()