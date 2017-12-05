
"""
 *****************************************************************************
   FILE:            bots.py

   AUTHOR:          Xingyu He

   ASSIGNMENT:      Project 9

   DATE:            Nov 5 2017

   DESCRIPTION:     There are two bots in the program. They move randomly and 
                    are able to change their attributes when they crash.

 *****************************************************************************
"""


from cs110graphics import *
import random


class Bot(object):

    def __init__(self, win, width, center, direction='east', speed=20):

        self._width = width
        self._center = center
        self._direction = direction
        self._speed = speed
        self._win = win

        cx = self._center[0]
        cy = self._center[1]

        # I learn how to use dictionary in swift.

        # CITE: https://docs.python.org/3/tutorial/datastructures.html
        # DETAIL: how to use dictionary and several basic methods relate to
        # dictionary type.

        # This is dictionary that indicates the correpsonding move for the 
        # parts in bot and the corresponding move for the cursor based on the
        # current direction. 
        self._directions_dict = {'north': ((0, -speed),(0, -round(width / 2))),
                                'east': ((+speed, 0), (round(width / 2), 0)),
                                'south': ((0, +speed), (0, +round(width / 2))),
                                'west': ((-speed, 0), (-round(width / 2), 0))}
        self._directions = ['north', 'east', 'south', 'west']

        # The following are the graphic objects in the bot object. 

        # Here is the rectangle
        self._rect = Square(win, width, center)

        self._rect.set_border_color('yellow')
        self._rect.set_fill_color('yellow')

        # Here is the direction cursor.
        self._direction_cursor = Circle(win, round(width / 10),
            (cx + self._directions_dict[self._direction][1][0],
             cy + self._directions_dict[self._direction][1][1]))

        self._direction_cursor.set_fill_color("green")

        # Here is the two eyes, two retinas, and two cromeas. 
        radius = round(self._width / 4)
        self._left_eye = Circle(win, radius, (cx - radius, cy))
        self._right_eye = Circle(win, radius, (cx + radius, cy))

        self._left_cromea = Circle(win, round(radius / 2), (cx - radius, cy))
        self._right_cromea = Circle(win, round(radius / 2), (cx + radius, cy))

        self._left_cromea.set_fill_color('black')
        self._right_cromea.set_fill_color('black')

        self._left_retina = Circle(win, round(radius / 4), (cx - radius, cy))
        self._right_retina = Circle(win, round(radius / 4), (cx + radius, cy))

        self._right_retina.set_fill_color('aqua')
        self._left_retina.set_fill_color('aqua')

        self._right_retina.set_border_color('aqua')
        self._left_retina.set_border_color('aqua')

        self._parts = [self._rect, self._direction_cursor, self._right_cromea,
                        self._left_cromea, self._right_eye, self._left_eye,
                        self._right_retina, self._left_retina]

    def update_dict(self):
        """update the dictionary whenever speed changes."""

        self._directions_dict = {'north': ((0, -self._speed), 
                                    (0, -round(self._width / 2))),
                                'east': ((+self._speed, 0), 
                                    (round(self._width / 2), 0)),
                                'south': ((0, +self._speed), 
                                    (0, +round(self._width / 2))),
                                'west': ((-self._speed, 0), 
                                    (-round(self._width / 2), 0))}

    def add_to_window(self):
        """add every part in the bot to the window."""

        for part in self._parts:
            self._win.add(part)

    def add_handler(self, handler):
        """add handler to every part of the bot."""

        for part in self._parts:
            part.add_handler(handler)

    def move(self):
        """move every part of the bot depends on the current direction."""

        cx = self._center[0]
        cy = self._center[1]

        # dx and dy is extracted from the dictionary. The key of the dictionary
        # is the current direction. 
        dx = self._directions_dict[self._direction][0][0]
        dy = self._directions_dict[self._direction][0][1]

        for part in self._parts:
            part.move(dx, dy)

        # update the center whenever the bot moves.
        self._center = (cx + dx, cy + dy)

    def turn_left(self):
        """This function makes the bot to turn left."""

        cx = self._center[0]
        cy = self._center[1]

        # Here is the mechanism of the dictionary.
        # First I find the index of the current direction within the direciton
        # list(self._directions). 
        # Second I find the next index of direction in the list and change the 
        # current direction to that direction. I use a modular process so that 
        # the index would not go out of bound. 
        # Finally, based the new direction, I am able to move the direction 
        # cursor to different position. I am also able to move the bot to a 
        # different position if I want to in my move(self) function. 

        direction_keys_Index = self._directions.index(self._direction)

        self._direction = self._directions[(direction_keys_Index - 1) %
        len(self._directions)]

        # Here, I move the direction cursor to a different position based on 
        # the current direction.
        self._direction_cursor.move_to(\
        (cx + self._directions_dict[self._direction][1][0],
        cy + self._directions_dict[self._direction][1][1]))

    def turn_right(self):
        """This function makes the bot to turn right."""

        cx = self._center[0]
        cy = self._center[1]

        # The same mechanism work here.
        direction_keys_Index = self._directions.index(self._direction)

        self._direction = self._directions[(direction_keys_Index + 1) %
            len(self._directions)]

        # Here, I move the direction cursor to a different position based on 
        # the current direction. 
        self._direction_cursor.move_to(\
        (cx + self._directions_dict[self._direction][1][0],
        cy + self._directions_dict[self._direction][1][1]))

    def speed_up(self):
        """This function speeds up the bot."""

        self._speed += 5
        # update dictionary whenever speed_up.
        self.update_dict()

    def slow_down(self):
        """This function speeds up the bot."""

        self._speed -= 5
        # update dictionary whenever speed_down. 
        self.update_dict()

    def crash(self):
        """This function is called whenever bot crash."""

        self._parts[0].set_fill_color("red")

    def uncrash(self):
        """This function is called whenever bot is not crashed."""

        self._parts[0].set_fill_color("white")

    def get_width(self):
        """Return the width of the bot"""

        return self._width

    def get_center(self):
        """Return the center of the bot"""

        return self._center

    def overlaps(self, other):
        """This returns whether the bot is overlapped with another lap."""

        # Here is the machanism for deciding whether the bot is overlapped. 
        # if the distance in the x and y direction between two centers of the 
        # bots is less than the average of the width, the two bots are 
        # overlapped. Vice Versa.

        self_cx = self._center[0]
        self_cy = self._center[1]

        other_cx = other._center[0]
        other_cy = other._center[1]

        # This represents the distance in the x and y direction. 
        distance_x = abs(other_cx - self_cx)
        distance_y = abs(other_cy - self_cy)

        sum_width = self._width + other.get_width()

        # check if the distance in the x and direction between the centers 
        # is less than the average of the width of two bots. 
        if distance_x < sum_width / 2 and distance_y < sum_width / 2:
            return True

        else:
            return False


class BotHandler(EventHandler):

    def __init__(self, bot):

        EventHandler.__init__(self)
        self._bot = bot

    def handle_mouse_release(self, event):
        """Whenever the mouse is clicked, the function is called."""

        number = random.choice([0, 1, 2])
        # Here is how the mechanism works: the number variable is assigned 
        # every time with a random number between 0, 1, and 2. Each number 
        # indicates whether the bot is turning left, right, or move. 

        if number == 0:
            self._bot.turn_left()

        elif number == 1:
            self._bot.turn_right()

        else:
            self._bot.move()


def program(win):

    bot1 = Bot(win, 100, (100, 200))
    bot1.add_to_window()

    bot2 = Bot(win, 100, (250, 200), 'west')
    bot2.add_to_window()

    bot1.add_handler(BotHandler(bot1))
    bot2.add_handler(BotHandler(bot2))


def main():

    StartGraphicsSystem(program)

if __name__ == "__main__":
    main()
