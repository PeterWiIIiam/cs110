"""
 *****************************************************************************
   FILE:        alphabet.py

   AUTHOR:      Xingyu He

   ASSIGNMENT:  Project 03 alphabet

   DATE:        09/09/2017

   DESCRIPTION: This program prints out the characters that are not in a 
                string. 

 *****************************************************************************
"""


def main():

    textOnSigns = str(input('Enter some text:'))
    UpperCaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UncommonLetter = ''

    #for every charcater that is in the alphebet 
    for char in UpperCaseAlphabet:
    #for every character that is not in the uppercase of textOnsigns
        if char not in textOnSigns.upper():
    #concetnate with each other to for uncommon letter 
            UncommonLetter = UncommonLetter + char

    print(' Letters not in the text: %s'%UncommonLetter)

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
