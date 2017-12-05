""" This is just the setup for a Nim game. """

from cs110graphics import *
import random

class Bean(EventHandler):
    """ We represent Beans with Circle objects. Beans can be clicked. """

    def __init__(self, win, radius, color, bgcolor, location, on, game):
        """ The Constructor for a Bean. """

        EventHandler.__init__(self)   # so that we may click Beans

        self._win = win
        self._radius = radius
        self._color = color
        self._bgcolor = bgcolor       # color of window background
        self._location = location     # of form (x, y)
        
        self._body = Circle(win, self._radius, self._location)
        self._body.set_fill_color(self._color)

        self._body.add_handler(self)

        self._activated = False

        self._game = game


    def handle_mouse_release(self, _):
        """ If a Bean is clicked, we turn it off, and change its color
            to the background color to hide the Bean. """

        if self._activated:
            self._body.set_fill_color(self._bgcolor)
            self._body.set_border_color(self._bgcolor)

            self._game.activate()

            self._color = self._bgcolor

        
    def activate(self):
        self._activated = True

    def deactivate(self):
        self._activated = False

    def activated(self):
        return self._activated

    def get_color(self):
        return self._color

class Game(object):

    def __init__(self, win, winheight, bgcolor):
        """ The Constructor for the Game. """

        self._win = win
        self._win.set_height(winheight)
        self._win.set_background(bgcolor)

        self._bgcolor = bgcolor

        bean_radius = 10   # radius of a bean
        bean_vspace = 30   # vertical spacing between beans in a heap
        heap_num = 0       # for horizontal location of a heap
        max_beans = 6      # maximum number of beans in a heap
        bean_color = 'mediumorchid'

        leftalign = 150    # x coordinate of leftmost heap
        space = 50         # number of pixels between heaps
        bottom = 300       # y coordinate of lowest bean

        # We create a list of random numbers for heap sizes:
        heap_sizes = []
        for _ in range(3):
            rnd = random.randint(1, 6)
            heap_sizes.append(rnd)

        print('heap_sizes is', heap_sizes)  # For debugging

        # We create the beans and place them in a grid. Each heap is
        # a list, and the lowest bean in the heap is first in the list.
        heap_grid = []
        for heap in range(3):
            heap_list = []
            for bean in range(max_beans):
                xloc = leftalign + (heap * space)
                yloc = bottom - (bean * bean_vspace)
                new_bean = Bean(self._win, bean_radius, bean_color, 
                                bgcolor, (xloc, yloc), True, self)
                heap_list.append(new_bean)
            heap_grid.append(heap_list)

        # Add the beans to the window:
        for heap in heap_grid:
            for bean in heap:
                win.add(bean._body)

        # Deactivate beans according to the heap_sizes list:
        for heap in heap_grid:
            heap[-1].activate()

        self._heap_grid = heap_grid


    def get_bgcolor(self):
        """ Returns the background color of the Game window. """
        return self._bgcolor


    def activate(self):
        print(1)
        for heap_num in range(len(self._heap_grid)):
            print(2)
            for bean in range(len(self._heap_grid[heap_num])):
                print(3)
                if self._heap_grid[heap_num][bean].get_color() == self._bgcolor:
                    self._heap_grid[heap_num][bean - 1].activate()
                    print(0)





def program(win):
    """ A game is created, and everything else happens within it. """
    Game(win, winheight=600, bgcolor='lavenderblush')


def main():
    StartGraphicsSystem(program)


if __name__ == "__main__":
    main()