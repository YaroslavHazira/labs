from utils import test

# https://www.codewars.com/kata/5b93fecd8463745630001d05
# The snail crawls up the column. During the day it crawls up some distance. During the night she sleeps, so she slides down for some distance (less than crawls up during the day).

# Your function takes three arguments:

# The height of the column (meters)
# The distance that the snail crawls during the day (meters)
# The distance that the snail slides down during the night (meters)
# Calculate number of day when the snail will reach the top of the column.

def snail(dd, dn, height):
    days = 0
    distance = height

    if dd >= height: 
        return 1

    while distance > 0:
        distance = distance - (dd - dn)
        days = days + 1
        # print("days", days)
        # print("distance", distance)
    
    days = days - 1 

    return days
    
test(3 , snail(2, 1, 4)) 
test(1 , snail(3, 1, 3))

test(1 , snail(2, 1, 2)) 
test(2 , snail(2, 1, 3))    
test(3 , snail(2, 1, 4))
test(5 , snail(2, 1, 6)) 


