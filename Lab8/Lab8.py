import turtle


def main():

    #greet("Howdy")
    #greet("Hi", "Alice")
    #greet("beep boop", name="robot")
    #print_triangle(5)
    #print(area_of_rectangle(5))

    # Call the functions you are testing here.
    #fractal_main()
    #print(enigma('hiking'))
    #print(conundrum(4))
    print(reverse('123456'))

def greet(greeting, name="person"):
    print(greeting, name)


def fractal_main():
    t = turtle.Turtle()
    t.speed(0)

    # turtle.tracer(False)

    t.setheading(90)
    fractal(t, 200)

    # turtle.update()

    turtle.mainloop()  # Prevents the screen from closing automatically.

def area_of_rectangle(width,length=None):
    if length:
        return width*length
    else:
        return width**2

def print_triangle(row,char='*'):
    if row== 1:
        print(char)
    else:
        print(char*row)
        print_triangle(row-1,char)

def fractal(t, length, level=2):

    TURNS = 5
    ANGLE = 144
    LENGTH_REDUCTION = 3

    if level == 0:
        return

    for _ in range(TURNS):
        t.forward(length)
        fractal(t, length / LENGTH_REDUCTION, level - 1)
        t.backward(length)
        t.left(ANGLE)


def enigma(string):
    if string == "":
        return ""
    elif string[0] in "aeiou":
        return string[0] + enigma(string[1:])
    else:
        return enigma(string[1:])


def conundrum(x):
    if x <= 0:
        return 1
    else:
        return conundrum(x - 1) * 2

def reverse(string,reverse_string=[]):
    if len(string) == 1:
        return string

    reverse_string.append(string[-1])
    reverse(string[:-1],reverse_string)


    

main()
