def add(x , lst = None):
	if lst == None:
		lst = []
	if x not in lst:
		lst.append(X)

	return lst
def main():
	list1 = add(1)
	print(list1)

	list2 = add(2)
	print(list2)

	list3 = add( 3 , [11,12,13 , 14])
	print(list3)

	list4 = add(4)
	print(list4)
main()

#difference between this code and the last bit of code is that the last bit had a defined list to append to, here it does not
#as such the output will differ 
