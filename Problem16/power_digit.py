"""power_digit.py: Problem 16 of project Euler.
Calculates the sum of the digits of the number 2^1000."""

if __name__ == "__main__":
    FULL_NUMBER = pow(2, 1000)
    TOTAL = 0

    for number in str(FULL_NUMBER):
        TOTAL += int(number)

    print "The sum of the digits of 2^1000 is {0}".format(TOTAL)

