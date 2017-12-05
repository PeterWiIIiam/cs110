"""
 *****************************************************************************
   FILE:        pizzas.py

   AUTHOR:		  Xingyu He		
	
   ASSIGNMENT:	Project 2 Pizzas

   DATE:      	Sept 7 2017

   DESCRIPTION:	

 *****************************************************************************
"""


def main():

    import math

    standard_diameter=float(input('What '
      'is the diameter of a "standard" size pie? '))
    standard_sliceperpie=int(input('How '
      'many slices are in a standard size pie? '))
    standard_slicedesired=int(input('How '
      'many standard slices do you want? '))
    supper_diameter=float(input('What '
      'is the diameter of the pies you will buy? '))

    #Calculate the total area desired
    total_area=(standard_diameter/2)**2*math.pi\
      /standard_sliceperpie*standard_slicedesired
    #Calculate the area of one supper pizza
    supper_area=(supper_diameter/2)**2*math.pi
    #Calculate the number of supper pizzas needed and round up
    supper_number=math.ceil(total_area/supper_area)

    print('You will need to buy %i %i-inch '
      'diameter pies.'%(supper_number,supper_diameter))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
