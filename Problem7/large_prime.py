"""large_prime.py: Problem 7 of project Euler.
Calculates the 10 001st prime number. """

import math

def is_prime_number(num):
    """ Determines whether the number provided is prime, or not. """

    sqtnum = math.sqrt(num)

    i = 2

    while i <= sqtnum:
        if num % i == 0:
            return False
        i = i+1

    return True

PRIME_COUNT = 1
LAST_PRIME = 2
CURRENT_NUMBER = 3

while PRIME_COUNT < 10001:
    if is_prime_number(CURRENT_NUMBER):
        LAST_PRIME = CURRENT_NUMBER
        PRIME_COUNT += 1

    CURRENT_NUMBER += 2

print "The 10001st prime number is {0}".format(LAST_PRIME)

