globalVar = 1 # creating a global variable
def f1():
	localVar = 2 
	print(globalVar)
	print(localVar)

f1()
print(globalVar)
print(localVar) # this is out of the scope of the local variable so it produce an error 


# V 2
x = 1 
def f1():
	x =  2 
	print(x) # displays 2 since3 it is within the function


f1() # displays 2 
print(x)  #displays 1 since it never undergoes the change from 1 to 2 
# in this example x is the global variable and it can undergo changes when put into a function 

#v3 

x = eval(input("Enter a number:"))
if x > 0:
	y = 4 

print(y) 
# here the program runs fine if you input a positive number for x 
# however, if you put 0 or a negative number, te program gives no output 

#v4 
sum = 0 
for i in range(5):
	sum += i 
	# the variable i is created within the loop itself 
	#after the loop is done, the sum is four so 