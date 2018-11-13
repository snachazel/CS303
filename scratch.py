print(format("num = 100" , "<17s") , end = " ")
  print("Calculated PI =", format( computePI(100) , "7.6f") , end = " ")
  print ( "Difference =" , "{0:+f}".format( computePI(100) - math.pi,  "7.6f"))
count = 100
while count <= 10000000:
  print(format(("num = " , count) , "<17s") , end = " ")
  print("Calculated PI =", format( computePI(count) , "7.6f") , end = " ")
  print ( "Difference =" , "{0:+f}".format( computePI(count) - math.pi,  "7.6f"))
  count *= 10

  



  numThrows = 100
  while numThrows <= 10000000:
    print(format(("num = " , numThrows) , "<17s") , end = " ")
    print("Calculated Pi = " , end = " ")
    print(format(computePI(numThrows)- math.pi , "7.6f") , end = " ")
    print ( "Difference =" , "{0:+f}".format( computePI(numThrows) - math.pi,  "7.6f"))
    numThrows *= 10

  print(format("num = 100" , "<17s") , end = " ")
  print("Calculated PI =", format( computePI(100) , "7.6f") , end = " ")
  print ( "Difference =" , "{0:+f}".format( computePI(100) - math.pi,  "7.6f"))

  print(format("num = 1000" , "<17s") , end = " ")
  print( "Calculated PI =", format( computePI(1000) , "7.6f"), end = " ")
  print ( "Difference =" , "{0:+f}".format( computePI(1000) - math.pi,  "7.6f"))

  print(format("num = 10000" , "<17s") , end = " ")
  print( "Calculated PI =", format( computePI(10000) , "7.6f"), end = " ")
  print ( "Difference =" , "{0:+f}".format( computePI(10000) - math.pi,  "7.6f"))

  print(format("num = 100000" , "<17s") , end = " ")
  print( "Calculated PI =", format( computePI(100000) , "7.6f"), end = " ")
  print ( "Difference =" , "{0:+f}".format( computePI(100000) - math.pi,  "7.6f"))

  print(format("num = 1000000" , "<17s") , end = " ")
  print( "Calculated PI =", format( computePI(1000000) , "7.6f") , end = " ")
  print ( "Difference =" , "{0:+f}".format( computePI(1000000) - math.pi,  "7.6f"))

  print(format("num = 10000000" , "<17s") , end = " ")
  print("Calculated PI =", format( computePI(10000000) , "7.6f") , end = " ")
  print ( "Difference =" , "{0:+f}".format( computePI(10000000) - math.pi,  "7.6f"))
