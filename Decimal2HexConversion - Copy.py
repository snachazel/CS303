#convert a decimal to a hex as a string
def decimalToHex(decimalValue):
	hex = ' '

	while decimalValue != 0:
		hexValue = decimalValue % 16
		hex = toHexChar(hexValue) + hex
		decimalValue = decimalValue // 16

	return hex
#converts the integer into a single hex digit
def toHexChar( hexValue):
	if 0 <= hexValue <= 9:
		return chr(hexValue + ord('0'))
	else:   # hex value from 10 to 15
		return chr(hexValue - 10 + ord('A'))

def main():
	decimalValue = eval(input( "Enter a decimal integer : "))

	print("The hx number for decimal" , decimalValue , "is" , decimalToHex(decimalValue))

main()

# hex string is initially empty (line 3)
#lines 2- 10 convert a decimal integer into a hex integer 
# remainder from line 6 is converted into a hex string in line 7 using ASCII
#lines 13-17 then turn hexvalue between 0 and 15 into a hexxx character 

