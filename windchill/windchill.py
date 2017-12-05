"""
 *****************************************************************************
   FILE:        windchill.py

   AUTHOR:		  Xingyu He	

   ASSIGNMENT:	Project 1 windchill calculator

   DATE:	     	Aug 29 2017

   DESCRIPTION:	Calculate windchill given the speed of the wind and the temperature. 

 *****************************************************************************
"""


def main():


  PLAINTX = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  CYPHERT = 'LNUTD XFIVMGAKPJSZRYWBECQOH'

  message = input("Enter a message with only uppercase and space: ")
  encrypted = ''

  for letter in message:
    letter = CYPHERT[PLAINTX.index(letter)]
    encrypted = encrypted + letter


  print("Your encrypted message follows:")
  print(encrypted)

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
