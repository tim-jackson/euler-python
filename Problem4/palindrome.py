"""palindrome.py: Problem 4 of project Euler.
Calculates the largest product of two 3-digit numbers"""

HIGH_TOTAL = 0
FIRST_DIGIT = 999

def is_palindrome(number):
    """ Checks if the number supplied is palindromic. """

    # Reverse the strip using ::-1
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    while FIRST_DIGIT != 0:
        SECOND_DIGIT = 999
        while SECOND_DIGIT != 0:
            TOTAL = FIRST_DIGIT * SECOND_DIGIT
            if is_palindrome(TOTAL):
                if TOTAL > HIGH_TOTAL:
                    HIGH_TOTAL = TOTAL
                SECOND_DIGIT -= 1
            else:
                SECOND_DIGIT -= 1
        FIRST_DIGIT -= 1

    print "Highest palindromic multiple: {0}".format(HIGH_TOTAL)

