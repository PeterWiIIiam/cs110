"""
 *****************************************************************************
   FILE:        checkerboard.py

   AUTHOR:      Xingyu He   

   ASSIGNMENT:  Project 6 checkerboard

   DATE:        Oct 8 2017

   DESCRIPTION: This program draws a black and white checkboard and a blue and 
                white checkerboard. 
 *****************************************************************************
"""

import turtle


def main():
    t = turtle.Turtle()
    t.speed(0)

    t.up()
    t.goto(-200, -200)
    t.down()
    draw_checkerboard(t, 50, 8, (60, 60, 0))

    t.up()
    t.left(30)
    t.forward(50)
    t.down()
    draw_checkerboard(t, 10, 10, "blue")

    turtle.mainloop()


def draw_square(t, length):
    """Use t to draw a square with length."""

    for count in range(4):
        t.forward(length)
        t.left(90)


def draw_checkerboard(t, length, squares_per_side, color):
    """Use t to draw a checkerboard with squares_per_side. The length of each 
    small square is length. The color of the checkerboard is color."""

    original_position = t.position()
    for row in range(1,squares_per_side+1):
        #this for loop controls the row of the checkerboard.length
        for square_num in range(squares_per_side):
            #this for loop draws individual square in the checkerboard.
            if (square_num%2 == 0 and row%2 != 0)\
            or (square_num%2 != 0 and row%2 == 0):
                #this if statement determines what color the small squares in 
                #checkerboard will be filled. The conditions control so that 
                #squares in both rows and columnes are spaced with white squares
                t.begin_fill()
                t.fillcolor(color)

            draw_square(t,length)
            t.end_fill()
            t.forward(length)
        #the following code makes the turtle to go upward to draw the other row.
        t.up()
        t.goto(original_position)
        t.left(90)
        t.forward(length*row)
        t.right(90)
        t.down()


main()
