def main():
	x = 1 
	print("Before the call, x is " , x)
	increment(x)
	print("After the call, x is " , x )

def increment (n):
	n += 1
	print("\tn inside the function is  " , n)
main()

# all data are objects in python , variable for object is actually reference to object itself 
# when you invoke a function, the reference value of each argument is passed to the parameter defined within the function 
# this is defined as the pass by value of the function 
# X(1) is passed to the parameter n in order to invoke the increment function
# n is changed by x is unchanged no matter what 