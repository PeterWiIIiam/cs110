"""
 *****************************************************************************
   FILE:        microwave.py

   AUTHOR:      Xingyu He

   ASSIGNMENT:  Project 3 microwave 

   DATE:        Sept 14 2017

   DESCRIPTION: This program takes the input of a time and counts down.

 *****************************************************************************
"""


def main():

    time = str(input('Enter the digits as input to the microwave: '))
    Index_Colon = time.index(':')
    #extract the number for minute
    minute = int(time[0:Index_Colon])
    #extract the number for second
    second = int(time[Index_Colon+1:])

    #both minute and second have to be positve or equal to zero
    while second >= 0:
        print('%i:%02i'%(minute,second))
    #print the current time and then the second goes down one
        second = second - 1
    #if the second is negative, that means that before that it is 0
    #that means that minute needs to be one less, and second return to 59
        if second < 0 and minute>0:
            minute = minute-1
            second = 59

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
