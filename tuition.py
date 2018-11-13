def main():
	year = 0 #initializing variable
	tuition = 10000 # year 1 tuition 

	while tuition < 20000:
		tuition = tuition * 1.07
		year += 1 
	print("Tuition will be doubled in ", year , "years.")
	print("Tuition will be $" , format(tuition , ".2f") ,  year, "years.")
main()

# the while loop coninuously computes tuition until it is greater than 20,000
# keeps track of how many years it takes due to the year = variable and the year += 1 assignment 