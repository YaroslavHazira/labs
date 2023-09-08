from utils import test

# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af

# DESCRIPTION:
#       Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

#       For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

#       Constraint:

#       1 <= month <= 12


def quaters(month):
    quater = 0

    if month <= 4:
        quater = 1
    if month > 4 and month <= 8:
        quater = 2
    if month > 8 and month <= 12:
        quater = 3
    
    return quater


test(1 , quaters(2))
test(2 , quaters(6))
test(3 , quaters(10))