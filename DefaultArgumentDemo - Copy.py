def printArea(width = 1 , height = 2):
	area = width * height
	print( "width:" , width , "\theight:" , height , "\tarea" , area)

printArea() #default argument
printArea(4 , 2.5) # positional arguments, meaning arugments are the same as defined in function and are input in the same order
printArea( height = 5 , width = 3) # keyword arguments meaning that the keywords in the parameters are match with the input keywords in this line
printArea( width = 1.2 ) #default argument using previously defined height
printArea( height = 6.2) #default argument used of width = 1 

#function may mix default and non default parameters. in this case, non default must be defined befroe default 
# default values are passed to the parameters when a function is invoked without arguments 