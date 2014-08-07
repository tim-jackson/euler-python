"""multiples.py: Exercise 1 of project Euler.
Calculates the sum of the multiples of 3 or 5, below 1000. """

if __name__ == "__main__":
    TOTAL = 0

    for num in xrange(0, 1000):
        if num % 5 == 0 or num % 3 == 0:
            TOTAL += num

    print "The sum of the multiples between 3 and 5, " \
                "below 1000 is: " + str(TOTAL)

