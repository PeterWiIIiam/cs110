"""
 *****************************************************************************
   FILE:            additive_primes.py

   AUTHOR:          Xingyu He

   ASSIGNMENT:      Project 7 additive_primes

   DATE:            Oct 19 2017

   DESCRIPTION:     This program has two function. The first is to determine 
                    whether a number is additive. The second is to output a list
                    of additive prime numbers within the range of 1 and the 
                    number

 *****************************************************************************
"""


# CITE: http://prime-numbers.wikia.com/wiki/Additive_Primes
# DETAILS: definition of additive prime numbers


def main():
    pass


def prime_number(n):
    """This function takes a number and determines whether it is a prime number
    """

    if n > 1:

        for divisor in range(2,n):

            if n%divisor == 0:
                #if n and divisor cannot complete full division, n is not a 
                #prime number

                return False

        return True

    else:
        #negative number is not prime number

        return False


def sum_digits(n):
    """This function takes a number and sums up its digits"""
    
    string_number = str(n)
    #convert n to a stirng so that we can iterate through its digit in a for 
    #loop
    summ = 0

    for digit in string_number:
        #go through each digit and add them together. 

        summ += int(digit)

    return summ


def additive_prime(n):
    """This function takes a number and determines whether it is an additive
    prime number"""

    if n<10:
        #for single digit number, we can use prime_number to test whether it is 
        #a prime number. It is the base case of the recursive function since 
        #the sum of the digits make a number closer to single digit number.

        return prime_number(n)

    else:

        if prime_number(n):
            #input the sum of the digits of the number as the input of the next
            #recursive call so that the return value will be the return value of 
            #the last recursive call. 

            return additive_prime(sum_digits(n))
        
        else:
            # if it is not a prime number, return false. 

            return False


def additive_primes_list(n):
    """This function finds the additive prime numbers between 0 and n. """
    
    primte_list = []
    
    for i in range(1,n+1):
        #the range is inclusive of 1 and n itself.

        if additive_prime(i):
            #compile all the additive prime numbers to a list.
            
            primte_list.append(i)

    return primte_list


if __name__ == "__main__":
    main()
