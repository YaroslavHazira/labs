# Your function takes two arguments:

# current father's age (years)
# current age of his son (years)

# Сalculate how many years ago the father was twice as old as his son 
# (or in how many years he will be twice as old). The answer is always greater or equal to 0,
# no matter if it was in the past or it is in the future.

def twice_as_old(dad_age, son_age):
    result = dad_age - son_age * 2
    if result < 0:
        print((result - result) - result, "years later his dad was twice as old as his son")
    else:
       print(result, "years ago his dad was twice as old as his son")


test = twice_as_old(38, 11)