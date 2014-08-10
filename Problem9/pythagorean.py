"""pythagorean.py: Problem 9 of project Euler. 
Finds the Pythagorean triplet such that a + b + c = 1000. """

import math

MAX_VALUE = 1000

def check_tuple(side_one, side_two, side_three):
    """ Checks whether the square of the first two sides
        equals that of the third. """

    if (pow(side_one, 2) + pow(side_two, 2)) == pow(side_three, 2):
        result = side_one*side_two*side_three
        print "Tuple Found: ({0}, {1}, {2})".format(side_one,
                                                    side_two, side_three)
        print "Product: {0}".format(result)

        return True
    else:
        return False

def calculate_tuples(side_one, side_two, side_three, max_value):
    """ Goes through the potential matching tuples where a<b<c. """

    while side_three < max_value:
        temp_a = side_one
        temp_b = side_two

        while temp_a < max_value and temp_b > 1:
            temp_a += 1
            temp_b -= 1
            if check_tuple(temp_a, temp_b, side_three):
                break

        temp_a = side_one
        temp_b = side_two

        while temp_b < max_value and temp_a > 1:
            temp_a -= 1
            temp_b += 1
            if check_tuple(temp_a, temp_b, side_three):
                break

        side_three += 1
        if side_two > 1:
            side_two -= 1
        else:
            side_one -= 1

# Work out which initial values or a, b and c to start with
EXACT = float(MAX_VALUE) / 3
ONE_START = math.floor(EXACT)
TWO_START = math.floor(EXACT)
THREE_START = math.ceil(EXACT)

calculate_tuples(ONE_START, TWO_START, THREE_START, MAX_VALUE)

