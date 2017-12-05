"""
 *****************************************************************************
   FILE:        wordfind.py

   AUTHOR:      Xingyu He

   ASSIGNMENT:  wordfind

   DATE:        Sept 26 2017

   DESCRIPTION: This program find the words in a list in a letter matrix and then 
                capitalize them.

 *****************************************************************************
"""


def printGrid(grid):
    """ Display the grid in a nice way """
    for row in grid:
        print(row)

def wordfind(myGrid, words):
    """ For each word in words, if possible, find it once in the grid, case 
        insensitive.  Convert those found letters in the grid 
        to upper-case."""
    
    # (For you to implement)
    count = 0
    left = [0,-1]
    right = [0,1]
    up = [-1,0]
    down = [1,0]
    upright = [-1,1]
    upleft = [-1,-1]
    downright = [1,1]
    downleft = [1,-1]
    directions = [left,right,up,down,upright,downright,upleft,downleft]

    for numberOfword in range(len(words)):
        all_possible_letters =[]
        letters_capitalize = []
        for letter in range(0,len(words[numberOfword])):
            coordinates_letter = []
            for y in range(len(myGrid)):
                for x in range(len(myGrid[y])):
                    if myGrid[y][x] == words[numberOfword][letter]\
                    or myGrid[y][x] == words[numberOfword][letter].upper():
                        coordinates_letter.append([y,x])
            all_possible_letters.append(coordinates_letter)


        for direction in directions:
            if findLetters(all_possible_letters,direction):
                if len(findLetters(all_possible_letters,direction)) == len(all_possible_letters):
                    letters_capitalize = findLetters(all_possible_letters,direction)

        if letters_capitalize != []:
            count += 1
        captalize(myGrid,letters_capitalize)
    return count

#check if it is vertical


def findLetters(all_possible_letters,direction):
    y = direction[0]
    x = direction[1]
    list_first_letter = all_possible_letters[0]
    for i in range(0, len(list_first_letter)):
        letters_capitalize = [list_first_letter[i]]
        if len(letters_capitalize) == len(all_possible_letters):
            return letters_capitalize
        for n in range(1,len(all_possible_letters)):
            for g in range(0,len(all_possible_letters[n])):
                if all_possible_letters[n][g][0] == letters_capitalize[-1][0] + y:
                    #check if it is in order 
                    if letters_capitalize[-1][1] == all_possible_letters[n][g][1] + x:
                        letters_capitalize.append(all_possible_letters[n][g])
                        print(all_possible_letters[n][g])
                    if len(letters_capitalize) == len(all_possible_letters):
                        return letters_capitalize


def captalize(myGrid,letters_capitalize):
    for wordCoordinate in letters_capitalize:
        xCoordinates = wordCoordinate[1]
        yCoordinates = wordCoordinate[0]
        myGrid[yCoordinates][xCoordinates] = myGrid[yCoordinates][xCoordinates].upper()


def main():
    """ The main program is just for your own testing purposes.
        Modify this in any way you wish.  It will not be graded. """
    
    myGrid = [['j', 'm', 'w', 'e'],#Y0
            ['e', 'e', 'p', 'p'],#Y1
            ['q', 'o', 'x', 'u'],#Y2
            ['w', 'w', 'e', 'd'],#Y3
            ['w', 'g', 'j', 'o']]#Y4
            # X0   X1   X2   X3

    words = ['meow', 'wed', 'do', 'epow']
    count = wordfind(myGrid, words)
    printGrid(myGrid)
    print(count)


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
