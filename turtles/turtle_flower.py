"""
 *****************************************************************************
   FILE:           turtle_flower.py

   AUTHOR:          Xingyu He

   ASSIGNMENT:      Project 6 turtle_flower.py

   DATE:            Oct 8 2017

   DESCRIPTION:     This program draws a flower with petals of different shapes.

 *****************************************************************************
"""

import turtle


def main():
    """Main function to test your functions.
    You may put any code you like here."""

    t = turtle.Turtle()
    t.shape("turtle")
    t.pencolor("blue")

    # Uncomment if you want the turtle to go fast!
    t.speed(0)

    #draw_flower(t,my_petal,)
    draw_flower(t,draw_pentagon,50,10)

    # Uncomment to draw a parallelogram, once implemented
    t.up()
    t.goto(0, -100)
    t.down()
    draw_parallelogram(t, 150, 70, 50)

    # Uncomment to draw a flower
    t.up()
    t.goto(200, 200)
    t.down()
    t.pencolor("red")
    draw_flower(t, draw_square, 50,10)

    # Uncomment to draw a flower with 6 petals, once implemented
    t.up()
    t.goto(-200, 200)
    t.down()
    draw_flower(t, draw_pentagon, 50, 6)

    # Uncomment to draw a flower with your my_petal function, once implemented
    t.up()
    t.goto(-200, -200)
    t.down()
    draw_flower(t, my_petal, 50, 8)


    turtle.mainloop()


def draw_square(t, length):
    """Draws a square with length."""
    for count in range(4):
        t.forward(length)
        t.left(90)


def draw_pentagon(t, length):
    """Draws a pentagon with length."""
    for count in range(5):
        t.forward(length)
        t.left(72)


def draw_parallelogram(t, length1, length2, angle):
    """Draws a parallelogram. First side has length = length1,
    second side has length = length2, and angle is the angle of
    the first turn the turtle makes."""
    for count in range(2):
        #this forloop draws the connecting two side of the parallelogram twice. 
        t.left(angle)
        t.forward(length1)
        t.left(180-angle)
        t.forward(length2)


def draw_flower(t, petal_shape, length,petla_number):
    """Draws a flower with length."""
    for petal in range(petla_number):
        petal_shape(t, length)
        t.left(360/petla_number)


def my_petal(t, length):
    """Draws a petal. May or may not use length.
    Note: the turtle must return to its original position and heading
    at the end of drawing the petal; otherwise, this won't work with
    draw_flower at arbitrary positions and headings."""
    for count in range(50):
        t.forward(length/5)
        t.left(360/100)


if __name__ == "__main__":
    main()
