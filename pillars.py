# There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Your function accepts three arguments:

# number of pillars (≥ 1);
# distance between pillars (10 - 30 meters);
# width of the pillar (10 - 50 centimeters).
# Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar).

def count_pillars(count, wieght, lenghts):
    result = (wieght + (lenghts + wieght) * (count - 1))
    print(result)
    return result

def test(expect, testResult):
    if(expect == testResult):
        print("Test pass: ", expect, testResult)
    else: 
        print("Test fail: ", expect, testResult )

test(1100 , count_pillars(2, 50, 1000))
test(2150 , count_pillars(2, 50, 1000))