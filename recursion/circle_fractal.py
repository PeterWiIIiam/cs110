"""
 *****************************************************************************
   FILE:  			circle_fractal.py

   AUTHOR:			Xingyu He	
	
   ASSIGNMENT:		Project 7 circle_fractal

   DATE:			Oct 18 2017

   DESCRIPTION:		This program draws the fractal of circl in a triangular 
   					position. 
			
 *****************************************************************************
"""


# CITE: https://docs.python.org/2/library/turtle.html
# DETAILS: method to draw a circle in turtle graphics. 


import math
import turtle


def main():

    t = turtle.Turtle()
    t.speed(0)

    level = int(input("Enter the level: "))
    circle_fractal(t,(0,0),200,level)

    turtle.mainloop()


def pos_before_draw(t,radius):
	"""This function goes to the beinning position to draw each circle"""

	t.up()
	t.setheading(270)
	t.forward(radius)
	t.down()
	t.setheading(0)
	#return to the original heading


def pos_center(t,center):
	"""This function goes to the center of a circle"""

	t.up()
	t.goto(center)
	t.down()


def draw_cricle(t,center,radius):
	"""This function draws a circle at a center and a radius"""

	pos_center(t,center)
	pos_before_draw(t,radius)
	t.circle(radius)


def circle_fractal(t,center,radius,level):
	"""This function draws circle fractals at center, with a radius. The 
	complexity of the fractal depends on the level"""

	if level == 0:
		#This is my base case. Whenever level is deducted to 0, a circle is 
		#drawn. There is no further recursion. 

		draw_cricle(t,center,radius)

	else:
		#This is my recursive case.

		draw_cricle(t,center,radius)
		#A circle is drawn when a recursion occurs. 


		deltaX = math.sqrt(3)*radius/2
		deltaY = radius/2
		#deltaX and deltaY are the change in position of the circles in the next
		#recursion call.


		center_left = center[0]-deltaX,center[1]-deltaY
		#center_left represents the center of the circle for the circle on the
		#left in the next level.

		center_right = center[0]+deltaX,center[1]-deltaY
		#center_right represents the center of the circle for the circle on the
		#right in the next level.

		center_up = center[0],center[1]+radius
		#center_left represents the center of the circle for the circle on the
		#left in the next level.

		radius = radius/2
		#the radius of the circles in the next level halves. 
		level -= 1 
		#The level decreases as recursion goes on and can finally reach the 
		#base case. 


		circle_fractal(t,center_right,radius,level)
		#the first recursion call is for the circle that is going to be on the 
		#right.
		circle_fractal(t,center_left,radius,level)
		#the second recursion call is for the circle that is going to be on the 
		#left.
		circle_fractal(t,center_up,radius,level)
		#the thrid recursion call is for the circle that is going to be on the 
		#top. 

		#one recursion call is always embedded with three recursion call inside
		#it until it reaches the base case. One circle is drawn every time 
		#recursion function is called. Therefore, one circle will lead to 
		#three smaller circles until the base case is reached. 


if __name__ == "__main__":
    main()
