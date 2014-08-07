"""fibonacci.py: Problem 3 of project Euler.
Calulates the sum of the even valued Fibonacci terms, under 4 million. """

FIRST_PREVIOUS = 1
SECOND_PREVIOUS = 2
UPPER_LIMIT = 4000000

# Total initially 2, as this is the first even prime number
TOTAL = 2

if __name__ == "__main__":
    while True:
        NEXT_NUMBER = FIRST_PREVIOUS + SECOND_PREVIOUS

        if NEXT_NUMBER >= UPPER_LIMIT:
            break

        if NEXT_NUMBER % 2 == 0:
            TOTAL += NEXT_NUMBER

        FIRST_PREVIOUS, SECOND_PREVIOUS = SECOND_PREVIOUS, NEXT_NUMBER

    print "The sum of all even valued terms under {0}, is " \
                "{1}".format(UPPER_LIMIT, TOTAL)

