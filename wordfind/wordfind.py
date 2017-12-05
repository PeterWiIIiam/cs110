"""
 *****************************************************************************
   FILE:        wordfind.py

   AUTHOR:      Xingyu He

   ASSIGNMENT:  wordfind

   DATE:        Sept 26 2017

   DESCRIPTION: This program find the words in a list in a letter matrix and 
                then capitalize them.

 *****************************************************************************
"""


def printGrid(grid):
    """ Display the grid in a nice way """
    for y in grid:
        print(y)


def wordfind(myGrid, words):
    """ For each word in words, if possible, find it once in the grid, case 
        insensitive.  Convert those found letters in the grid 
        to upper-case."""
    
    # (For you to implement)
    count = 0
    #each tuple has the changing values of y and x to indicate the direction
    #of the word.
    directions = [(0,-1),(0,1),(-1,0),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    letters_capitalize = []

    for numberOfword in range(len(words)):      
        word = words[numberOfword]
        all_possible_letters = find_all_possible_letters(words,myGrid,word)
        for direction in directions:
            #if the letter_to_be_capitalized can find letters to be capitalize,
            #assign the return value to letter_capitalize. Count the word every
            #time this condition is met.
            #I learn optional values in swift 3 and I did not search on the web.
            #This is a way to prevent function to return nil and crash the 
            #program.
            if letters_to_be_capitalized(all_possible_letters,direction):
                letters_capitalize.extend(\
                letters_to_be_capitalized(all_possible_letters,direction))
                count += 1
                #once the capitalize_letters can return once, which means that
                #the word is found in one direction, the loop breaks.
                break
                
    captalize(myGrid,letters_capitalize)
    return count


def find_all_possible_letters(words,myGrid,word):
    """This function finds the coordinates of letters of word in words. For 
    example. If the word is meow, the function finds the coordinates of all 
    the "m","e","o","w" in myGrid """

    all_possible_letters =[]

    for letter in word:
        #initialize coordinates_letter every time so that it only carries 
        #possible coordinates for one letter.
        coordinates_letter = []
        for y in range(len(myGrid)):
            for x in range(len(myGrid[y])):
                #Find the same letter from word in the grid. The letter in 
                #the grid could be capitalized since it could be found prior.
                if myGrid[y][x] == letter\
                or myGrid[y][x] == letter.upper():
                    #append the possible coordinates of one letter.
                    coordinates_letter.append([y,x])
        #append the possible coordinates of letters of each word.
        all_possible_letters.append(coordinates_letter)
    return all_possible_letters


def letters_to_be_capitalized(all_possible_letters,direction):
    """This function finds the coordinates of letters in a single word that will
    be capitalized. """

    Delta_y = direction[0]
    Delta_x = direction[1]
    list_first_letter = all_possible_letters[0]

    #first_letter is the coordinate of each possible first letter. There could 
    #be multiple first letters.
    for first_letter in list_first_letter:
        #the first coordinate of letters_capitalize is the possible coordinates 
        #of the first letters 
        letters_capitalize = [first_letter]

        #if the length of the letters_capitalize is the length of all_possible_
        #letters, there is no further test to find the next letter because 
        #there is only one letter.
        if len(letters_capitalize) == len(all_possible_letters):
            return letters_capitalize 
        for possible_coordinates in all_possible_letters[1:]:
            #possible_coodinates represents the coordinates in the list of 
            #possible coordinates of each letter. 
            for coordinate in possible_coordinates:
                #coordinate represent each coordinate for one letter.
                #coordinate_Y is the Y value of current coordinate. 
                #letters_capitalize[-1][0]represents the y value of the last 
                #coordinate in letters_capitalize. desired_Y represents the 
                #the desired Y value for the direction give.
                #Same mechanism applies to x value. 
                coordinate_Y = coordinate[0]
                coordinate_X = coordinate[1]
                desired_Y = letters_capitalize[-1][0]+Delta_y
                desired_X = letters_capitalize[-1][1]+Delta_x

                if coordinate_Y == desired_Y\
                and coordinate_X == desired_X:
                    letters_capitalize.append(coordinate)
                #when letters_capitalize append the last letter of the word,
                #it returns the entire list of coordinates. 
                if len(letters_capitalize) == len(all_possible_letters):
                    return letters_capitalize


def captalize(myGrid,letters_capitalize):
    """This function takes a word grid and coordinates for letters to be
    capitalized and capitalize those letters.
    """

    for wordCoordinate in letters_capitalize:
        #This for loop go through every coordinate in letters_capitalize.
        #it goes through x and y value for every coordinate.
        xCoordinates = wordCoordinate[1]
        yCoordinates = wordCoordinate[0]

        #find the corresponding letter in myGrid with the coordinates and 
        #convert the letters to upper case.
        myGrid[yCoordinates][xCoordinates]\
        = myGrid[yCoordinates][xCoordinates].upper()


def main():
    """ The main program is just for your own testing purposes.
        Modify this in any way you wish.  It will not be graded. """
    
    #I use x and y to indicate column and row.
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
