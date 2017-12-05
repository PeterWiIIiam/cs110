"""
 *****************************************************************************
   FILE:        pool.py

   AUTHOR:		Xingyu He

   ASSIGNMENT:	Project 2 Pool

   DATE:		Spet 7 2017

   DESCRIPTION:	Cal

 *****************************************************************************
"""


def main():

    pool_length = float(input('Pool length (feet): '))
    pool_width = float(input('Pool width (feet): '))
    additional_desired_depth_in_inches = float(input('Additional'
      ' depth desired (inches): '))
    rate=float(input('Water fill rate (gal/min): '))

    additional_desired_depth_in_feet=additional_desired_depth_in_inches/12

    #CITE: https://www.google.com/(search cubic feet to gallon)
    #DETAILS: Conversion from cubic feet to gallon 1 cubic feet*576/77=1 gallon
    volume=pool_width*pool_length*additional_desired_depth_in_feet*576/77

    total_time_in_minute=volume/rate

    hour=int(total_time_in_minute//60)
    minute=int((total_time_in_minute-hour*60)//1)
    second=round((total_time_in_minute-hour*60-minute*1)*60)

    print('Time: %02.i:%02.i:%02.i'%(hour,minute,second))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
