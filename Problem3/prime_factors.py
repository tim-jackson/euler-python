"""prime_factors.py: Exercise 3 of project Euler.
Calculates the largest prime factor of 600851475143. """

import math

INPUT_NUMBER = 600851475143
FACTOR = 2
OUTPUT = 0

def is_prime_number(number):
    """ Determines whether the number provided is prime. """

    sqtnum = math.sqrt(number)

    i = 2
    while i <= sqtnum:
        if number % i == 0:
            return False
        i = i+1

    return True

if __name__ == "__main__":
    if is_prime_number(INPUT_NUMBER):
        OUTPUT = INPUT_NUMBER
    else:
        while INPUT_NUMBER != FACTOR:
            while INPUT_NUMBER % FACTOR == 0 and INPUT_NUMBER != FACTOR:
                INPUT_NUMBER = INPUT_NUMBER / FACTOR

            if INPUT_NUMBER != FACTOR:
                FACTOR = FACTOR + 1
                while is_prime_number(FACTOR) == False:
                    FACTOR = FACTOR + 1
            OUTPUT = FACTOR

    print "The largest factor is " + str(OUTPUT)

