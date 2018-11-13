def main():
	import random

	numberoftrials = 1000000
	numberofhits = 0 # initializing the changing variable 

	for i in range( numberoftrials):
		x = random.random() * 2 - 1
		y = random.random() * 2 - 1 

		if x * x + y * y <= 1:
			numberofhits += 1
	pi = 4 * numberofhits / numberoftrials
	print(" Pi is ", pi)
main()

#how does this work?
# program generates a random floating pont (random.random() generates float) that is multiplied by 2 and turned into a decimal for x and y 
# if x^2 and y^2 give a sum less than 1, they are inside the circle with radius 1 
# an approximation of pi is roughly 4 * hits / trials 