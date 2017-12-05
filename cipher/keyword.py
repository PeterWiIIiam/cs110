"""
 *****************************************************************************
   FILE:        decrypt.py

   AUTHOR:      Xingyu He

   ASSIGNMENT:  Project 4

   DATE:        20 09 2017

   DESCRIPTION: This program takes an encrypted message and a keyword and 
                outputs an decrypted message 

 *****************************************************************************
"""

def remove_spaces(text):
    """ Given string   text  , build and return a new string with all
    spaces removed.  For example, from "Happy birthday   to you", return
    "Happybirthdaytoyou" """

    captured_text_list =[]

    for char in text:
        #select the character in a string that is not a space.
        if char != " ":
            #form a new list of the characters in the text without space.
            captured_text_list.append(char)

    return captured_text_list



def subtract(text, key):
    """ Given two uppercase letters of the alphabet, determine and return the
    unencrypted letter from the encrypted_letter was generated using
    key_letter.  For example, when encrypted_letter is "J" and key_letter is
    "R", return "S". """ 

    '''We create an associated number with key and text based on their orders in 
    append'''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index_text = alphabet.index(text)
    index_key = alphabet.index(key)

    #determine whether add 26 when subtract from index of key from index of text
    index_decrepted = index_text - index_key 
    if index_decrepted < 0 :
        #if the result of subtraction is negative, add 26
        index_decrepted = index_decrepted + 26 
    decrypted_character = alphabet[index_decrepted]

    return decrypted_character



def decrypt(text, key):
    """ For each letter in   text  , determine the letter from which it was 
    encrypted using   key  . Build and return the string of these letters."""

    concatante_decrypted_text = ''
    n = 0

    for i in text:
        '''For each element in text, a list, it is put in into the subtract
        function as text
        For each character in key, it is put in into the subtract function 
        as key'''
        key_character = key[n]
        decryptedCharacter = subtract(i,key_character)
        n = n + 1 

        '''If the index of the character in the key equals the length of the key
        the value of n is reset to 0 so that key can be repeated'''
        if n == len(key):
            n = 0
        concatante_decrypted_text += decryptedCharacter

    return concatante_decrypted_text



def report(message, clues):
    """ Print the   message  , and, for each clue in   clues  , if it occurs in 
      message  , indicate so on the output. """

    print("The decrypted message is", message)
    for entry in clues:
        if entry in message:
            print('Clue', entry, 'discovered in', message)


def main():
    """
    This function is provided in full. Its job is to control
    the flow of the program, and offload the details to the
    other functions.
    """
    
    captured_text = input('Enter the captured text: ')
    keyword = input('Enter a keyword: ')
    clues = input('Enter the clues separated by one space: ')
    clueList = clues.split();

    # Take all spaces out of the captured text:
    squished_text = remove_spaces(captured_text)

    # Send the captured text for decryption:
    decrypted_text = decrypt(squished_text, keyword)

    # Check the decrypted text for clues that indicate a real message.
    report(decrypted_text, clueList)


# Here we invoke the main function. This code is always included in our
# python programs.
if __name__ == "__main__":
    main()
