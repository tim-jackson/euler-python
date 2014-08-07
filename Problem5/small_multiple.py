"""small_multiple.py: Problem 5 of project Euler.
Calculates the smallest integer which is divisible by the
numbers 1-20 inclusive. """

# Given in the question as smallest number that has factors 1-10
# Therefore we can discard the numbers 1-10 as any factor of 1-20
# must also be divisble by this number
CURRENT_NUM = 2520
STEP = 2520
FACTORS = [11, 13, 14, 16, 17, 18, 19, 20]

def is_even_divisible(number):
    """ Checks if a number is divisable by all numbers up to 20. """

    return all(number % n == 0 for n in FACTORS)

if __name__ == "__main__":
    while (True):
        if is_even_divisible(CURRENT_NUM):
            print "The smallest positive number divisible by all " \
                        "numbers from 1-20 is {0}".format(CURRENT_NUM)
            break
        else:
            CURRENT_NUM = CURRENT_NUM + STEP

