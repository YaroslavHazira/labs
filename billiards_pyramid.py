from utils import test

# https://www.codewars.com/kata/5bb3e299484fcd5dbb002912
# Remember the triangle of balls in billiards? To build a classic triangle (5 levels) you need 15 balls. With 3 balls you can build a 2-level triangle, etc.

# For more examples,
# pyramid(1) == 1
# pyramid(3) == 2
# pyramid(6) == 3
# pyramid(10) == 4
# pyramid(15) == 5
# Write a function that takes number of balls (≥ 1) and calculates how many levels you can build a triangle.


def pyramid(balls):
    # levels = 0
    # levelBalls = 0
    # while balls > levelBalls:
    #     levels = levels + 1
    #     levelBalls = levelBalls + levels
        # print("levels", levels)
        # print("levelBalls", levelBalls)

    levels = 0
    count = balls
    while count > 0:
        levels = levels + 1
        count = count - levels
        # print("levels ", levels)
        # print("count", count)

    return levels


test(1 , pyramid(1))
test(2 , pyramid(3))
test(4 , pyramid(7))
test(4 , pyramid(10))
test(5 , pyramid(15))