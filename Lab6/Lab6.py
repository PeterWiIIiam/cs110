# Skeleton program for Lab 6 (Perkins)

import turtle
import random

def main():
    # The turtle is named  t  here in main(), and you should
    # pass it to each function, where I call the turtle  trixie .
    t = turtle.Turtle()

    # Call functions from here.
    #dots(t)
    #triangles(t)
    #squares(t)
    #nest(t,200)
    draw_nest_square(t,100,50)
    turtle.mainloop()  # Prevents the screen from closing automatically.


def dots(trixie):
    """
    Argument list:

    trixie = the name of the turtle

    This function draws a palette of dots that is intended to guide
    the viewer to an understanding of the three numbers used when
    colormode = 255.
    """
    trixie.hideturtle()
    trixie.speed('fast')
    for y in range(0, 255, 10):
        for x in range(0, 255, 10):
            trixie.up()
            trixie.goto(x, y)
            trixie.down()
            trixie.color(x, y, 0)
            trixie.dot(10)


def triangles(trixie):
    """
    Argument list:

    trixie = the name of the turtle

    The function's purpose is kept hidden for now, because we
    would like you to decipher it by reading.
    """
    trixie.width(5)
    for x in range(-100, 100, 40):
        draw_equil(trixie, x, 0, 40)
    trixie.hideturtle()


def draw_equil(trixie, x, y, size):
    """
    Argument list:

    trixie = the name of the turtle
    x, y = pixel at the start of drawing
    size = length of one side of the triangle

    The function's purpose is kept hidden for now, because we
    would like you to decipher it by reading.
    """
    trixie.up()
    trixie.goto(x, y)
    trixie.pencolor('black')

    trixie.fillcolor('red')
    trixie.begin_fill()
    trixie.down()
    for i in range(3):
        trixie.forward(size)
        trixie.left(120)
    trixie.end_fill()

def squares(t):
    t.width(10)
    for x in range(-100,150,50):
        draw_square(t,x,0,50)

    

def draw_square(t,x,y,size):
    t.up()
    t.goto(x,y)
    t.pencolor(random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255))

    t.fillcolor(random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255))
    t.begin_fill()
    t.down()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


def nest(trixie, nom):
    """
    Argument list:

    trixie = the name of the turtle
    nom = a number that controls the current pencolor
    """
    if nom > 20:
        trixie.width(5)
        trixie.pencolor(nom, nom, nom)
        trixie.up()
        trixie.home()
        trixie.down()
        trixie.setheading(0)
        for _ in range(3):
            trixie.forward(nom)
            trixie.left(120)

        nest(trixie, nom - 20)

def draw_nest_square(t,nom,init_size):
    if nom > 20:
        t.width(10)
        t.color(nom,nom,nom)
        t.up()
        t.setheading(45)
        t.forward(20)
        t.setheading(0)
        t.down()
        increment = 20/(2**(1/2))
        for _ in range(4):
            t.right(90)
            t.forward(init_size+increment*2)
        draw_nest_square(t,nom-10,init_size+increment*2)
def dice(trixie):
    number = int(input('Enter a number from 1 to 6: '))
    # Feel free to tinker with these settings:
    pip_size = 12 
    trixie.width(5)
    draw_square(trixie, 0, 0, 60)
    trixie.pencolor('black')

    # ...
    # Your code goes here!
    # ...
    # ...

    trixie.hideturtle()


def draw_pips(trixie, lst, size):
    """
    Argument list:

    trixie = the name of the turtle
    lst = a list of pip locations
    size = the size of each pip

    This function is called by dice() and will draw pips at
    specified locations within a square already drawn by dice().
    """
    for entry in lst:
        trixie.up()
        trixie.goto(entry)
        trixie.down()
        trixie.dot(size)


main()
