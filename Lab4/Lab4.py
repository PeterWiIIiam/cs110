""" LAB 4 """

# PART A:  Preliminaries

def main():
    print(divide_string("pick uo a brown cat", [3,8,12]))

def mystery(someList):
    answer = 1
    for item in someList:
        item = item * 2
        answer = answer * item
    print(someList)

def test_mystery():
    myList = [1, 2, 3]
    print(mystery(myList))
    print(myList)

def count(lst, item):
    """ Return the number of occurrences of item in lst. """
    assert type(lst) == list
    summ = int()
    for i in lst:
        if i == item:
            summ = summ + 1
    return summ


def locations(lst, item):
    """ Return a list of the indices i where lst[i] == item """
    assert type(lst) == list
    locationlist = []
    for i in range(len(lst)):
        if lst[i] == item:
            locationlist.append(i)
    return locationlist

# PART B:  Deriving the definition of "split"

# Read this function 
def locations_of_letter(letter, string):
    """ Build a list of all the locations of letter in string."""
    assert type(string) == str
    assert type(letter) == str and len(letter) == 1
    locations = []
    for i in range(len(string)):
        if string[i] == letter:
            locations.append(i)
    return locations

# Write a better version of locations_of_letter that finds the
# locations of any substring, not just a string of length 1.
# For example, locations_of("oo", "I was looking for a book") returns
# [7, 21]

def locations_of_substr(substr, string):
    """ Build a list of all the locations of letter in string."""
    assert type(string) == str
    assert type(substr) == str
    locationlist = []
    StringList = list(string)
    SubstringList = list(substr)
    for i in range(len(string)):
        if SubstringList[0] == StringList[i] and SubstringList[1] == StringList[i+1]:
                locationlist.append(i)
    return locationlist


def divide_string(string, positions):
    """ Return a list of substrings of string, the first one 
        beginning at position 0, the rest beginning at indices given in 
        positions.  For example, if string is "Pick up a brown cat" and
        positions is [3, 8, 12], this function returns 
        ['Pic', 'k up ', 'a br', 'own cat'] """
    assert type(string) == str
    assert type(positions) == list
    positionList = list(positions)
    for i in positionList:
        positionList.insert(0,0)
        substring1 = string[positionList[i-1]:positionList[i]]
        SliceStringList.append(substring1)
    return SliceStringList


# -------0---------0---------0---------0---------0---------0---------0---------0

# 3. Using the functions you've defined above, write a function that
#    splits a string according to a separator.
#    For example, split("12:56:19", ":") returns ["12", "56", "19"].
#    Hint:  first use locations_of_substr, then divide_string with
#    those locations.  Finally, replace all but the first
#    divided string with a slice removing the separator from the front.
def split(string, separator):
    assert type(string) == str
    assert type(separator) == str and len(separator) > 0
    pass
    
if __name__ == "__main__":
    main()

    
