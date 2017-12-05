"""
 *****************************************************************************
   FILE:        turtle_drawing.py

   AUTHOR:      Xingyu He

   ASSIGNMENT:  Project 6 trutle_drawing

   DATE:        Oct 8 2017

   DESCRIPTION: This program takes user input and execute the commands. Inputs 
                can make turtle to draw upwards, downwards, left, and right. 
                Turtle can change color and the length of each move. It can go
                directly to a location. 
 *****************************************************************************
"""

import turtle


distance = 30


def main():
    michelangelo = turtle.Turtle()
    turtle_drawing(michelangelo)


def turtle_drawing(t):
    """this turtle takes commands and draw acoording the commands """

    # This allows you to change the value of the global variable distance
    global distance

    print("\nThe commands are: w, a, s, d, color, distance, width, goto, quit")

    user_input = input("Enter a command: ")

    if user_input == "w":
        t.setheading(90)
        t.forward(distance)
    elif user_input == "a":
        t.setheading(180)
        t.forward(distance)
    elif user_input == "s":
        t.setheading(270)
        t.forward(distance)
    elif user_input == "d":
        t.setheading(0)
        t.forward(distance)
    elif user_input == "color":
        #ask user input and change the color of t
        color_input = input("Enter a color: ")
        t.color(color_input)

    elif user_input == "distance":
        #ask user input and change the distance each time turtl travels
        distance_input = input("Enter a distance: ")
        distance = float(distance_input)
    elif user_input == "width":
        #ask user input the width of turtle
        width_input = input("Enter width: ")
        t.width(float(width_input))
    elif user_input == "goto":
        #ask user input the coordinate t should be
        x_goto_input = input("Enter x-coordinate: ")
        y_goto_input = input("Enter y-coordinate: ")
        t.up()
        t.goto(float(x_goto_input),float(y_goto_input))
        t.down()
    elif user_input == "quit":
        return

    turtle_drawing(t)


main()
