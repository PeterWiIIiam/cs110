"""
 *****************************************************************************
   FILE:            zombies.py

   AUTHOR:          Xingyu He 

   ASSIGNMENT:      Project 8

   DATE:            Oct 29 2017

   DESCRIPTION:     In this game, we create a set of dice with varying sides and
                    put them randomly on two teams: vampires and zombies. The 
                    dice sit in a circular arrangement, so that each die has two
                    neighbors. On each game turn, all dice are rolled, and if 
                    any die's roll is less than a neighboring enemy's roll, that
                    die is converted to the other team.

                    The game continues until all dice belong to one team or all 
                    dice belong to one team!

                    The new changes are documented following:

                    User is able to create as many addtional teams other than 
                    the already existed Zombie and Vampire teams. The teams 
                    around the current team will compare their values and the 
                    team in the middle will change to the team of which the die
                    has the bigger value. 

                    For example, if the result of dice are 3,2,5, because∏ the 
                    die on the right is bigger than the die on the left, the 
                    die in the middle would change to the team that die on the 
                    right belong to.

                    The game ends when all the dice belong to one team.

 *****************************************************************************
"""


import random


class Die():
    """Represents a die for the vampires vs. zombies dice game.
    Each Die has a number of sides, a team, a location, and a value."""

    def __init__(self, sides, team, location, side_up=0):
        """ Constructor. """

        self._sides = sides
        self._team = team
        self._loc = location
        self._side_up = 0
        self._opponent = None

    def roll(self):
        """ We roll a die by choosing a  side_up . """

        self._side_up = random.randint(1, self._sides)

    def get_value(self):
        """ We check the value on the upward-facing side of the die. """

        return self._side_up

    def get_sides(self):
        return self._sides

    def get_team(self):
        return self._team

    def get_loc(self):
        return self._loc

    def change_team(self):
        """ This function changes the die's team. """

        self._team = self._opponent

    def set_opponent(self,team):
        """This function sets the oppositional team that is about to change."""

        self._opponent = team


class Game():
    """Plays the vampires vs. zombies dice game."""

    def __init__(self, num_dice,teams):
        """ Create dice and put them on teams at random.
            This function is provided in full to you."""

        self._num_dice = num_dice
        self._dice = []
        self._turn = 0
        self._teams = teams
        #I change the teams to attribute of the class so that it can be
        #modified and retrived in the functions of this class.

        sides_options = [4, 6, 8, 10]

        for loc in range(self._num_dice):
            sides = random.choice(sides_options)
            team = random.choice(teams)
            self._dice.append(Die(sides, team, loc))

    def __str__(self):
        """ We print a status report. 
            This function is provided in full to you. """

        to_print = ''
        for die in self._dice:
            this_die = ('die %3i: d%-2i (%7s) rolled %i' %
                        (die.get_loc(), die.get_sides(), die.get_team(),
                        die.get_value()))
            to_print = to_print + this_die + '\n'
        return to_print

    def get_turn(self):
        """ This function should return the turn number of the game. """

        return self._turn

    def increment_turn(self):
        """ This function should add 1 to the turn counter. """

        self._turn += 1

    def roll_all(self):
        """ This function should roll all of the dice. """

        for die in self._dice:
            die.roll()

    def is_game_over(self):
        """ We check for the end of the game, which happens when
            all dice are vampires or all dice are zombies. Here is how the check
            works. If every other die has the same die as the first die, the
            game is over."""

        first_die = self._dice[0]

        for die in self._dice:

            if die.get_team() != first_die.get_team():

                return False

        return True
        print('war is over')

    def update_teams(self):
        """ We see for each die if it should change teams.
            This function should call  check_battles(). 
            The function does not return anything. Instead, it
            should update the  self._dice  list."""

        battle_result = self.check_battles()

        for i in range(len(battle_result)):
            #check every result of the die and see if it needs to be changed

            if battle_result[i]:

                self._dice[i].change_team()



    def check_battles(self):
        """ We check the results of all possible battles.
        This function should call  attack_result() .
        The function should return the list  switch_teams , with
        each entry either True or False. """

        battle_result = []  

        for die in self._dice:
            battle_result.append(self.attack_result(die))
        return battle_result


    def attack_result(self, curr):
        """ Called by  check_battles , here we calculate the result
            of each battle, returning if the die should s.
            The function should return:
                True   if current die should switch teams and
                False  otherwise """

        die_value = curr.get_value()

        left_die = self._dice[curr.get_loc() - 1]
        #left_die represents the dat that is left to the curr die.


        right_die = self._dice[(curr.get_loc() + 1)%self._num_dice]
        #right_die represents the die that is right to the curr die. If the curr
        #die is the last die, because of the modular operation, right die of the 
        #last die in the list will be the first die in the list. 

        if curr.get_team() != left_die.get_team():
            #first check whether the team on the left and curr team
            #are the same.

            if die_value < left_die.get_value():
                #second check the values of each team.

                curr.set_opponent(left_die.get_team())
                #set the opponent that curr die  is about to change to.

                if curr.get_team() != right_die.get_team():
                    #the following component is to check whether the right_die's
                    #value is bigger than left_die's value. If it is true, 
                    #set_opponent is called on right die's team.

                    if die_value < right_die.get_value():

                        if right_die.get_value() > left_die.get_value():
                            curr.set_opponent(right_die.get_team())
                            #set the opponent that curr die  is about to change 
                            #to.

                return True

        if curr.get_team() != right_die.get_team():
            # first check whether the team on the right and curr team are the
            # same.

            if die_value < right_die.get_value():
                # second check the value of two dice.

                curr.set_opponent(right_die.get_team())
                # set the opponent that curr die  is about to change to.

                return True

        return False
        # if nothing happens, return False. No change will happen on this curr
        # die.


def main():
    """ We run the game from here. 
        This function is provided in full to you.  """

    print('More teams, more fun!')

    num_dice = int(input('Enter the number of dice to use in the war: '))
    addtional_team_num = \
    int(input('Enter the number of additional teams in the war: '))
    #ask the user the inputs for addtional teams

    teams = ["zombies","vampires"]

    for i in range(addtional_team_num):
        team = str(input('Enter the name of team %i: '%(i+3)))
        #prompt the user to enter the names of the new teams. 
        teams.append(team)

    war = Game(num_dice, teams)  
    # Change this number to change how many dice we use.

    while not war.is_game_over():
        war.increment_turn()
        war.roll_all()

        print('Turn', war.get_turn())
        print(war)

        war.update_teams()

    print()
    print('Final status after %i turns:' % war.get_turn())
    print(war)


if __name__ == "__main__":
    main()
