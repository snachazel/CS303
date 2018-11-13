def gcd(n1 , n2):
	gcd = 1 # initial gcd
	k = 2 # possilbe gcd

	while k <= n1 and k <= n2:
		if n1 % k == 0 and n2 % k == 0:
			gcd = k # update gcd

		k += 1 
	return gcd # return gcd