"""
 *****************************************************************************
   FILE:        ball.py

   AUTHOR:      Xingyu He

   ASSIGNMENT:  Project 3 ball

   DATE:        Sept 10 2017

   DESCRIPTION: This program takes the inital height, the height of the first
                bounce and the number of bounces and give the distance the 
                ball has travel.

 *****************************************************************************
"""


def main():

    #get the input flaues
    InitialHeight = float(input('Enter initial height: '))
    Height_FirstBounce = float(input('Enter height of first bounce: '))
    Number_Bounces = int(input('Enter number of bounces: '))
    NoOfTimesHitTheFloor = 0
    #compute the bounce index
    Index_bounce = Height_FirstBounce/InitialHeight

    #define variables that are ready to accumulate in the loop.
    distanceTravel = float()
    distanceFalling = float()
    distanceRising = float()
    totalDistance = float()

    '''for all the situation where the number bounces is less than the number of
    the bounces'''
    while NoOfTimesHitTheFloor < Number_Bounces:
        '''distance falling is equal to the distance of first falling times the 
        index raised to the number it has hit the floor'''
        distanceFalling = InitialHeight*Index_bounce**NoOfTimesHitTheFloor
        '''after the ball falls, it hit the floor one more time'''
        NoOfTimesHitTheFloor = NoOfTimesHitTheFloor+1
        '''distance rising is equal to the distance of first falling times the index
        raised to the number it has hit the floor'''
        distanceRising = InitialHeight*Index_bounce**NoOfTimesHitTheFloor
        '''distance traveled before and after a bounce is the sum of distance
        falling and distance rising'''
        distanceTravel = distanceFalling + distanceRising
        '''this line is used to accumulate the total distance traveled within 
        all the bounces'''
        totalDistance = distanceTravel + totalDistance

    totalDistance = round(totalDistance,2)

    print('The total distance the ball traveled is %s feet.'%(totalDistance))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
