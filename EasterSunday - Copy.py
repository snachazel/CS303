#  File: EasterSunday.py

#  Description: Compute Easter Sunday 

#  Student Name:Stephen Nachazel

#  Student UT EID: sdn443

#  Course Name: CS 303E

#  Unique Number: 53140

#  Date Created:9/ 13 / 2017
 
#  Date Last Modified: 9 / 18 / 2017

def main():
  
  #prompt user to enter year	
  y = eval(input(" Enter year: "))

  # compute Easter Sunday using Gaussian algorithm
  a = y % 19
  
  b = y // 100

  c = y % 100

  d = b // 4 

  e = b % 4 

  g = ( 8 * b + 13 ) // 25 

  h = ( 19 * a + b - d - g + 15) % 30
  
  j = c // 4 

  k = c % 4 

  m = ( a + 11 * h ) // 319

  r = ( 2 * e + 2 * j - k - h + m + 32) % 7 

  n = ( h - m + r + 90) // 25

  p = ( h - m + r + n + 19 ) % 32 

  # print day and month for Easter Sunday
  print(" ")
  
  if n == 3:

  	print(" In" , y , "Easter Sunday is on" , p , "March.")

  if  n == 4:
  	
  	print(" In" , y , "Easter Sunday is on" , p , "April.")

main()
