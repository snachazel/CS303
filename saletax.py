def main():
	purchaseamount= eval(input("Enter purchase amount:"))
	tax= purchaseamount * 0.06
	print("Sales Tax is ", int(tax * 100) / 100.00)

main()
