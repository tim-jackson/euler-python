"""primesum.py: Problem 10 of project Euler.
Calculates the sum of prime numbers below 2000000."""

# NOTE: This is quite slow. Need to reduce the pool of
# potential prime numbers dramatically.

import math

TOTAL = 2
I = 3
MAX_NUMBER = 2000000

def is_prime_number(number):
    """ Checks if a number is prime. """

    sqtnum = math.sqrt(number)

    j = 2
    while j <= sqtnum:
        if number % j == 0:
            return False
        j += 1

    return True

if __name__ == "__main__":
    while I < MAX_NUMBER:
        if is_prime_number(I):
            TOTAL += I
        I += 2

    print "The sum of prime numbers under {0} is {1}".format(MAX_NUMBER, TOTAL)

