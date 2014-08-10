"""square_difference.py: Problem 6 of project Euler.
Finds the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum. """

import math

COUNTER = 1
SQUARE_TOTAL = 0
SUM_NUMBERS = 0

while COUNTER <= 100:
    SUM_NUMBERS += COUNTER
    SQUARE_COUNTER = math.pow(COUNTER, 2)

    SQUARE_TOTAL += SQUARE_COUNTER
    COUNTER += 1

SQUARE_SUM = math.pow(SUM_NUMBERS, 2)
DIFFERENCE = SQUARE_SUM - SQUARE_TOTAL

print "Difference is: {0}".format(DIFFERENCE)

