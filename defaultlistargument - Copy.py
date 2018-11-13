def add(x , lst = []):
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

#function add appends x to lst if x not in the list
#when function is executed for the first time, the default value [] iscreated
#when list argument is given, this is passed to lst and supersedes an appeneded element in the function 
