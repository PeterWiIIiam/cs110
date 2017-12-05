"""
 *****************************************************************************
   FILE:        metricTime.py

   AUTHOR:		Xingyu He	

   ASSIGNMENT:	Project 2 MetricTime

   DATE:		Sept 7 2017

   DESCRIPTION:

 *****************************************************************************
"""


def main():

    import math

    Userinput = str(input('Enter the time of day '
      'in military time (HH:MM:SS): '))

    # CITE: Alex 
    # DETAILS: Format to search the second colon
    theFirstColon = Userinput.index(":")
    theSecondColon = Userinput.index(':',theFirstColon+1)

    Hourinput = int(Userinput[0:theFirstColon])
    Minuteinput = int(Userinput[Userinput.index(":")+1:theSecondColon])
    Secondinput = float(Userinput[theSecondColon+1:len(Userinput)])

    #First converting all seconds to metric seconds
    #Calculate the output seconds 
    SecondMetric = (Secondinput+Minuteinput*60+Hourinput*3600)/86400*100000
    SecondOutput = SecondMetric%100

    #Calculate the output minute
    MinuteMetric = SecondMetric//100
    MinuteOutput = MinuteMetric%10

    #Calculate the output hour
    HourOutput = MinuteMetric//10

    print('The "metric" time is:')
    print('%0.2i:%i:%05.2f'%(HourOutput,MinuteOutput,SecondOutput))
# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()

