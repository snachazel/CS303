def main():
	#using floating point numbers in the loop continuation may cause numerical errors which is an issue
	#initialize sum
	sum = 0
	#add .01 + 0.02 + ........ 0.99 , 1 to sum
	i = 0.01
	while i <= 1.0:
		sum += i
		i = i + 0.01

	print("The sum is" , sum)
main()


#program runs but the sum is incorrect. Why?
#The answer is that the final term ends up being slightly larger than 1 so it isn't used in the sum
#this is due to the fact that floating points are represented by approximations
# how to fix this?