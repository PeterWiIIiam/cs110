"""
 *****************************************************************************
   FILE:        watch.py

   AUTHOR:	   	Xingyu He

   ASSIGNMENT:	Project 2 Watch

   DATE:	     	Sept 7 2017

   DESCRIPTION:

 *****************************************************************************
"""


def main():

    Userinput = str(input('What time does your '
      'upside-down watch read (hours:minutes)? '))

    Hourinput = int(Userinput[0:Userinput.index(":")])
    Minuteinput = int(Userinput[Userinput.index(":")+1:len(Userinput)])

    #CITE: Christian TA 
    #DETAIL: use modular make anything hour below or equal to 6 to add 6
    HourOutput = (Hourinput+5)%12+1

    #CITE: Christian TA 
    #DETAIL: make anything in minute below 30 to add 30. When the Minuteinput is 30, output is 0
    MinuteOutput = (Minuteinput+30)%60

    print ('The right-side-up time is: %i:%02.i'%(HourOutput,MinuteOutput))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
